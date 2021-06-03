<?php
error_reporting(1);
ini_set("display_errors",1);
$connect = mysqli_connect("localhost", "root", "0976", "level1");

if(mysqli_connect_error()){
    echo "mysql 접속중 오류가 발생했습니다.";
    echo mysqli_connect_error();
}

$view_num = $_GET['idx'];
$sql = "SELECT * FROM sing_board WHERE idx = $view_num";
$result = mysqli_query($connect, $sql);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name = "viewport" content="width=device-width, initial-scale=1.0">
    <title> 글 수정 </title>
</head>

<body>
    <h1> 수정하기</h1>

    <?php
    if($row = mysqli_fetch_array($result)){
    ?>
    <form action="writePost_update.php" method="post">

        <input type="hidden" name="idx" value="<?= $view_num ?>">

        <p>
            <label for='name'> 이름 : </label>
            <input type="text" id = "name" name="name" value="<?= $row['name']?>">
        </p>
        <p>
            <label for='memo'> 내용 : </label>
            <textarea name="memo" id="memo" cols="30" rows="10"><?= $row['memo']?> </textarea>
        </p>
        <input type="submit" value="저장">
    </form>
   
    <?php }
    mysqli_close($connect);
    ?>
</body>
</html>




<a href="list.php">목록</a> 
