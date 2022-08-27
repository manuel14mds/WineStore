<?php
$destination= $_POST["name"];
$name = $_POST["name"];
$email = $_POST["email"];
$subjet = $_POST["subjet"];
$message = $_POST["message"];
$comentarios = $_POST["comentarios"];

$content = "Name: "  . $name . "\nEmail: "  . $email ."\nsubject: " . $subjet . "\nMessage: " . $message;
    
mail($destination,"contacto",$content);
?>