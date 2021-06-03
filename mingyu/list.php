<?php
    include "db.php";

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
    <h2>글 목록</h2>
    
    <form action="search_result.php" method="post">
    <h3>검색할 키워드를 입력하세요.</h3>
    <p>
        <label for="search">키워드:</label>
        <input type="text" id="search" name="skey">
        </p>
        <input type="submit" value="검색">
    </form>
  
    <form action="delete.php" method="post">
    <h3>삭제할 메시지 번호를 입력하세요.</h3>
    <p>
        <label for="search">키워드:</label>
        <input type="text" id="msgedl" name="delnum">
        </p>
        <input type="submit" value="삭제">
    </form>
  

<ul>
<?php
error_reporting(1);
ini_set("display_errors",1);
$connect = mysqli_connect("localhost", "root", "0976", "level1");

if(mysqli_connect_error()){
    echo "mysql 접속중 오류가 발생했습니다.";
    echo mysqli_connect_error();
}

$sql = "SELECT * FROM sing_board";
$result = mysqli_query($connect, $sql);
$list = '';
//리스트를 가져오는 코드(제목(a href) 을 클릭하면 View.php로 넘어감)
while($row = mysqli_fetch_array($result)){
    $list= $list."<li>{$row['idx']}:<a href=\"view.php?idx=
    {$row['idx']}\">{$row['subject']}</a> - {$row['memo']} - {$row['regdate']}</li>";

}
echo $list;
?>
</ul>
<a href="write.php">글쓰기</a> 
</body>
</html>