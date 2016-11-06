<?php

include("php_jumper/connector.php");

if(isset($_POST["mail"])){
    if(filter_var("iamjbn@gmail.com", FILTER_VALIDATE_EMAIL)){
        mysqli_query ( $link , "INSERT INTO `onetimenotify`(`email`, `tracker`) VALUES ('iamjbn@gmail.com','hi')") or die("error inserting");
echo "poooi";
   }
}


//to subscrice email
if(isset($_POST['email'])){
    if(filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)){
        $result = mysqli_query ( $link , "SELECT * FROM `onetimenotify` WHERE `email` ='".$_POST['email']."'");
        if(mysql_num_rows($result)){
            $result = mysqli_query ( $link , "INSERT INTO `onetimenotify`(`email`, `tracker`) VALUES ('".$_POST['email']."','".$text."')");
            if($result){
                echo '<div id="push_message_green" class="hideMe">
                        subscribed.
                        </div>';
            }else{
                echo '<div id="push_message_red" class="hideMe">
                        error subscribing.. we will fix it.
                        </div>';
            }
        }else{
            echo '<div id="push_message_red" class="hideMe">
                    already subscribed.
                    </div>';
        }
   }else{
       echo '<div id="push_message_red" class="hideMe">
        invalid email
    </div>';
    }
}




?>

<html>
    <form action="test.php" method="POST">
        <input name="email" type="email" required />
        <input type="submit" />
    </form>
</html>	