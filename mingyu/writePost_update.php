<?php 
    error_reporting(1);
    ini_set("display_errors",1);
    $connect = mysqli_connect("localhost", "root", "0976", "level1");
    
    if(mysqli_connect_error()){
        echo "mysql 접속중 오류가 발생했습니다.";
        echo mysqli_connect_error();
    }

    $name = $_POST['name'];
    $subject = $_POST['subject'];
    $memo = $_POST['memo'];
    $idx = $_POst['idx'];

    $name = mysqli_real_escape_string($connect, $name);
    $subject = mysqli_real_escape_string($connect, $subject);
    $memo = mysqli_real_escape_string($connect, $memo);
    
     
        $query = "update sing_board set name='$name',
        subject='$subject'
        memo='$memo'
        where idx='$idx'";

        mysqli_query($connect, $query);
?>
<script>
    location.href='list.php';
</script>

