<?php 
    include "db.php";

    $name = $_POST['name'];
    $subject = $_POST['subject'];
    $memo = $_POST['memo'];
    $idx = $_POst['idx'];

    $name = mysqli_real_escape_string($connect, $name);
    $subject = mysqli_real_escape_string($connect, $subject);
    $memo = mysqli_real_escape_string($connect, $memo);


    if($idx){
      
        $query = "update sing_board set name='$name',
        subject='$subject'
        memo='$memo'
        where idx='$idx'";

        
        mysqli_query($connect, $query);

    }else{



    $regdate = date("Y-m-d H:i:s");

    $query = "insert into sing_board(name, subject, memo, regdate)
        values('$name', '$subject', '$memo', '$regdate')";

        
    mysqli_query($connect, $query);
    }
?>
<script>
    location.href='list.php';
</script>

