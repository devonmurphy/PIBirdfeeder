<!DOCTYPE HTML>  
<html>
<body> 
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>

<button id="takePic">Take Picture</button>
<button id="clean">Delete Pictures</button>
<button id="birdfeeder">Start Birdfeeder</button>
<button id="stop">Stop Birdfeeder</button>
<p></p>
<script type="text/javascript">
  var interval = setInterval(function(){
	location.reload();
},10000);  
   $(document).ready(function(){
        $("#takePic").click(function(){
            $.ajax({
                type: 'POST',
                url: 'takePic.php',
                success: function(data) {
		    location.reload(); 
                }
            });
   });
	$("#clean").click(function(){
            $.ajax({
                type: 'POST',
                url: 'clean.php',
                success: function(data) {
		    location.reload(); 
                }
            });
   });
	$("#birdfeeder").click(function(){
            $.ajax({
                type: 'POST',
                url: 'birdfeeder.php',
                success: function(data) {
		    location.reload(); 
                }
            });
   });
	$("#stop").click(function(){
            $.ajax({
                type: 'POST',
                url: 'stop.php',
                success: function(data) {
		    location.reload(); 
                }
            });
 
   });

});
</script>


<?php
$imagesDir = '';
$images = glob($imagesDir . '*.{jpg,jpeg,png,gif}', GLOB_BRACE);
foreach ($images as $img){
        echo '<img src="./'.$img.'"style="width:480px;height:300px;" />';
}
?>
</body>
</html>
