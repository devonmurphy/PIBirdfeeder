<!DOCTYPE HTML>  
<html>
<body> 
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>

<button id="takePic">Take Picture</button>
<button id="clean">Delete Pictures</button>

<p></p>
<script type="text/javascript">
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
