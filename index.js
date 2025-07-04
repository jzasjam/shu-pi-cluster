var http = require('http').createServer(handler); //require http server, and create server with function handler()
var fs = require('fs'); //require filesystem module
var io = require('socket.io')(http, { allowEIO3: true }) //require socket.io module and pass the http object (server)
var path = require('path');
const csv = require('csv-parser');

//Using the standalone hw-specific library
let matrix = require('sense-hat-led');
//Using this library
//matrix = require('node-sense-hat').Leds;

// =====================================================================================
// Create a server
// =====================================================================================
http.listen(8080); //listen to port 8080
var os = require("os");
var hostname = os.hostname();
console.log("Server Running (http://"+hostname+":8080) (Ctrl+C to stop)");

// Handle The HTTP Requests (pages / css / imgs / csv / etc)
// =====================================================================================
function handler(request, res) { //create server

	var filePath = '.' + request.url;
	//console.log(filePath);
	if (filePath == './') {
		filePath = '/public/index.html';
	} else {
		filePath = '/public' + request.url;
	}
	//console.log(filePath);
	var extname = path.extname(filePath); //For routing different static files
	//console.log(extname);

	var contentType = 'text/html';
	switch (extname) {
		case '.js':
			contentType = 'text/javascript';
			break;
		case '.css':
			contentType = 'text/css';
			break;
		case '.csv':
			contentType = 'text/csv';
			break;
		case '.png':
			contentType = 'image/png';
			break;
		case '.gif':
			contentType = 'image/gif';
			break;
		default:
			console.log(filePath);
	}

	// Read The File and Serve It
	// =====================================================================================
	fs.readFile(__dirname + filePath, function (err, data) {

		if (err) {
			res.writeHead(404, { 'Content-Type': 'text/html' }); //display 404 on error
			return res.end("404 Not Found");
		}

		res.writeHead(200, { 'Content-Type': contentType });
		res.end(data, 'utf-8');
	});

}


// =====================================================================================
// WebSocket Connection (Handle The Client Requests)
// =====================================================================================
io.sockets.on('connection', function (socket) {// WebSocket Connection

	// Static variables for current status
	var lightvalue = 0; 
	var liveCharts;		// Static variable for the live chart interval

	// ==========================================
	// Light Up The SenseHat Pixels with Range Slider
	// ==========================================
	socket.on('light', function (data) { //get light switch status from client

		// Get the value from the slider (0-51) then multipy by 5 so (0-255)
		lightvalue = Number(data)*5;
		if (lightvalue!=0) {
			console.log("Lights On at "+((lightvalue/255)*100).toFixed(0)+"%");
			matrix.clear([lightvalue, lightvalue, lightvalue]);
		} else {
			console.log("Lights Off")
			matrix.clear();
		}

	});


	// ==========================================
	// Run A FogNode Cluster Test
	// ==========================================
	socket.on('test_cluster', function (data) {

		console.log("Testing Cluster")
		//console.log(data)

		// Set The Python Script Arguments
		args = ['--clusterjobs', data[0], '--colour', data[1], '--jobslength', data[2]]
		// Run the Python Script to Test the Cluster
		runPy('cluster-leds.py', args, 'cluster-test-log')

	});



	// ==========================================
	// Funtion To Run Python Scripts With Arguments
	// ==========================================
	function runPy(scriptPath, args, log=false) {

		console.log("Running Python Script: "+scriptPath)

		// Run the Python script
		const { PythonShell } = require('python-shell');
		
		let options = {
			mode: 'text',
			//pythonPath: 'path/to/python',
			pythonOptions: ['-u'], // get print results in real-time
			//scriptPath: 'path/to/my/scripts',
			args: args
		};

		PythonShell.run(scriptPath, options).then(messages => {
			// results is an array consisting of messages collected during execution
			//console.log('results: %j', messages);
			results = messages
			console.log(" PYTHON RESPONSES \n====================== ")
			// Collect results into string for log file
			var fullLogResults = ""
			var logResults = ""
			// Loop through results entry
			results.forEach((result) => {
				// Add the result to the logResults string
				if(!result.startsWith("[+]") && !result.startsWith("[X]")){
					logResults += result + "<br>"
				}
				fullLogResults += result + "<br>"

			});
			// Log the results to the console
			console.log(logResults)

			// Return The Results to a Log Div
			if(log){
				// Write the results to a log file
				/* fs.writeFile('public/'+log, logResults, function (err) {
					if (err) throw err;
					console.log('Message Event Logged');
				}); */
				socket.emit('log_update', [log, logResults, fullLogResults]);
			}
		});

	}

    

});
