<?php
    include "db.php";

?>

<ul>
<?php
error_reporting(1);
ini_set("display_errors",1);
$connect = mysqli_connect("localhost", "root", "0976", "level1");

if(mysqli_connect_error()){
    echo "mysql 접속중 오류가 발생했습니다.";
    echo mysqli_connect_error();
}

$user_delnum =$_POST['delnum'];

// 검색 기능 (memo를 제목으로 할지 내용으로할지 선택)
$sqlDEL = "DELETE FROM sing_board WHERE idx LIKE $user_delnum";
mysqli_query($connect, $sqlDEL);
$sql = "SELECT * FROM sing_board";
$result = mysqli_query($connect, $sql);
$list = '';

while($row = mysqli_fetch_array($result)){
    $list= $list."<li>{$row['idx']}:<a href=\"view.php?idx=
    {$row['idx']}\">{$row['subject']}</a> - {$row['memo']} - {$row['regdate']}</li>";

}
    echo $list;
    mysqli_close($connect);
?>
</ul>
<p>
<?php
    echo $user_delnum.'번째 데이터가 삭제되었습니다.';
?>
</p>
<a href="list.php">목록</a> 