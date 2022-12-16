<?php
$host="localhost";
$username="root";
$password="";
$database="suggestion_with_html_ajax";

$connection=mysqli_connect($host,$username,$password,$database);
$sql="SELECT * FROM names";
$results=mysqli_query($connection,$sql);
$array=array();
while($data=mysqli_fetch_assoc($results)){
    $array[]=$data;
}

echo json_encode($array)
?>