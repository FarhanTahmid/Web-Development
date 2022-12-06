<?php

    //For creating database at first!

    // $servername = "localhost";
    // $username = "root";
    // $password = "";
    
    // // Create connection if first attempt
    // $connection = new mysqli($servername, $username, $password);
    // if ($connection->connect_error) {
    //   die("Attempt to make connection failed! " . $connection->connect_error);
    // }
    
    // // Create database Cse-482-final
    // $sql = "CREATE DATABASE Cse_482_final";
    // if ($connection->query($sql) === TRUE) {
    //   echo "Database Cse-482-final created successfully!";
    // } else {
    //   echo "Error creating database!: " . $connection->error;
    // }
    
    // $connection->close();

    //Creating table
    $db=mysqli_connect("localhost","root","","Cse_482_final");
    if(!$db){
	    die("Database not connected"."<br>" ) ;

    }else{
        if(isset($_POST['submit'])){
            $username = $_POST["username"];
            $password = $_POST["password"];
            $re_password = $_POST["re-pass"];
            $contact = $_POST["contact"];
            $email = $_POST["email"];
            if ($password == $re_password) {
                $sql = "INSERT INTO customerdetails(username,password,contact,email)VALUES ('$username','$password','$contact','$email')";
                if (mysqli_query($db, $sql)) {
                    echo "Submission Successful!";
                } else {
                    echo "Error Submitting Form! Choose another Username." . mysqli_error($db);
                }
            }else{
                echo "Passwords Did not match!";
            }
        }
        if(isset($_POST['cancel'])){
            header("Refresh:0;url=form.html");
        }
    }

    //Creating table for the first time.
    // $sql="CREATE TABLE customerdetails (
    //     customer_id INT AUTO_INCREMENT NOT NULL  PRIMARY KEY,
    //     username varchar(50) NOT NULL UNIQUE,
    //     password varchar(50) NOT NULL,
    //     contact varchar(50),
    //     email varchar(50) NOT NULL
    // )"; 
    // if(mysqli_query($db,$sql)){
    //     echo "Table created";

    // }else{
	//     echo "There was an error while creating the table".mysqli_error($db);
    // }

?>