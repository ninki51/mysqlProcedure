<?PHP

/**
	获取连接
*/

function conn() {
    $dbh = new PDO("mysql:host=localhost;port=3306;dbname=shopDB", "root", "pwd1234", array(PDO::ATTR_PERSISTENT => false));
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $dbh->exec("set names utf8mb4");
    return $dbh;
}

//更新操作
function updateOp($id, $pwd , $new_pwd) {
    $count = 0;
    try {
        $dbh = conn();
        $sql = "UPDATE user set pwd=? WHERE id=? and pwd=?";
        $stmt = $dbh->prepare($sql);
        $stmt->execute(array($new_pwd, $id, $pwd));
        //$stmt->debugDumpParams();
        //print_r ($stmt->errorInfo());
        $count = $stmt->rowCount();
        $dbh = null;
    } catch (PDOException $e) {
        return -1;
    }
    return $count;
}

//获取list startNo=起始行号，pageSize=每页行数
function getUserList($startNo,$pageSize) {

    $dbh = conn();
    $sql = "SELECT id,name,group FROM user where id>(select id from user limit ?,1) limit ?";

    $PDO->setAttribute( PDO::ATTR_EMULATE_PREPARES, false );
    $stmt = $dbh->prepare($sql);
    $stmt->execute(array($startNo,$pageSize));
    //$stmt->debugDumpParams();
    //print_r ($stmt->errorInfo());
    //echo $stmt->errorCode();
    $data = array();
    while ($rs = $stmt->fetch(PDO::FETCH_OBJ)) {
        $row = array(
            'id' => $rs->id,
            'name' => $rs->name,
            'group' => $rs->group
        );
        array_push($data, $row);
    }
    $dbh = null;
    return $data;
}