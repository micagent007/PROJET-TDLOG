<script>
    var timeleft = {{time_left}};
    var downloadTimer = setInterval(function(){
        timeleft--;
        var seconds = timeleft % 60;
        var minutes = Math.floor(timeleft / 60);
        document.getElementById("countdown").textContent = minutes + " minutes " + seconds + " secondes";
        if(timeleft <= 0)
            clearInterval(downloadTimer);
    },1000);
</script> 