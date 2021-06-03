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
    <title> abc 게시판</title>
</head>

<body>
    <h1>게시판</h1>

    <?php
    if($row = mysqli_fetch_array($result)){
    ?>

        <h3> 글번호: <?= $row['idx']?>       제목: <?= $row['name']?></h3>
        <h2>글 내용 :</h2>
        <div> 
            <?= $row['memo']?>
        </div>

    <?php }
    mysqli_close($connect);
    ?>

<p><a href="list.php">목록</a> </p>
<p><a href="update.php?idx=<?= $row['idx']?>">수정하기</a> </p>

</body>
</html>