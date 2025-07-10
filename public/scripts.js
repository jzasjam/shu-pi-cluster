const socket = io(); //load socket.io-client and connect to the host that serves the page

$(document).ready(function () {
    
    // For each .chart_content hide if has no class .active
    $('.chart_content').each(function(){
        if(!$(this).hasClass('active')){
            $(this).hide();
        }
    });

    // Navigation Tabs
    $('ul.nav-tabs a.nav-link').click(function(){
        var tab_id = $(this).attr('attr-tab');

        $('ul.nav-tabs a.nav-link').removeClass('active');
        $('.tab-content').removeClass('active');

        $(this).addClass('active');
        $("#"+tab_id).addClass('active');
        
        $('.chart_content.active').removeClass('active').hide();
        $('#'+tab_id).addClass('active').show();

        return false;
    })

    
    // Sub Navigation Tabs
    $('ul.sub-tabs a.subnav-link').click(function(){
        var tab_id = $(this).attr('attr-tab');
        
        // Hide all subtabs
        $('ul.sub-tabs a.subnav-link.active').removeClass('active');
        $('.subtab-content.active').removeClass('active').hide();
        // Show the selected subtab
        $(this).addClass('active');
        $("#"+tab_id).addClass('active');
        $('#'+tab_id).addClass('active').show();

        return false;
    })
    
    // Sub Navigation Tabs
    $('a.subnav-link').click(function(){
        var tab_id = $(this).attr('attr-tab');
        
        // Hide all subtabs
        $('ul.sub-tabs a.subnav-link.active').removeClass('active');
        $('.subtab-content.active').removeClass('active').hide();
        // Show the selected subtab
        // Add .acctive clas to  ul.sub-tabs a.subnav-link with attr-tab
        $('ul.sub-tabs a.subnav-link[attr-tab="'+tab_id+'"]').addClass('active');
        
        
        $('#'+tab_id).addClass('active').show();
        
        return false;
    })


    
    
    // On change of the light slider light the leds
    $("#light").on('input change', function(){
        var light = $(this).val();
        socket.emit('light', light);
    });

    

    // Test The Cluster
    $('#test_cluster').click(function(){

        //if(confirm("This will test the Fog Node Cluster, are you sure? If you do not have any Servers / Fog Nodes available, this will fail!")){

            // Perform Task
            socket.emit('test_cluster', [$('#cluster-jobs').val(), $('#cluster-colour').val(), $('#jobs-length').val()]);

            // Waiting Message
            message = 'Testing The Cluster In Progress...<br>You should see the LEDs light up when a Server / Fog Node is working on a job...<br>Please Wait for the Results...';
            $('#cluster-test-log').html(message);
            $('#cluster-test-log-full').html(message);
            
            // Hide the Button (reshow once script has returned)
            $('#cluster-test-button').hide();
            $('#cluster-testing').show(); // Show the testing message
            // Reload the #cluster-status-iframe after 5 seconds
            // Get the current hostname
            const hostname = window.location.hostname;
            // Construct the iframe src URL
            const iframeSrc = `http://${hostname}:8181`;
            setTimeout(function(){
                $('#cluster-status-iframe-src').html(iframeSrc);
                $('#cluster-status-iframe').attr('src', iframeSrc);
                $('#cluster-status').show();
            }, 1000);
        //}
        
        return false;
    });

    // Close cluster status box
    $('#close-cluster-status').click(function(){
        $('#cluster-status').hide();
        return false;
    });
    

});


// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}


// Test Completed- Receive An Update For A Log
socket.on('log_update', function (data) {

    // data[0] is the id of the log div
    // data[1] is the message to appen
    $('#'+data[0]).html(data[1]); // Puts the logged message into the correct div
    $('#'+data[0]+'-full').html(data[2]); // Puts the logged message into the correct div
    // On CLuster Test completion
    if(data[0]=='cluster-test-log'){
        // Reshow Buttons on Completion
        $('#cluster-test-button').show();
        $('#cluster-testing').hide(); // Hide the testing message
    }

});