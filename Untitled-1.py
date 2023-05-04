

function    ()
	{
		$db['default']['hostname'] = "localhost";
		$db['default']['username'] = "abc";
		$db['default']['password'] = "123";
		$db['default']['database'] = "book";
		$conn = mysqli_connect($db['default']['hostname'], $db['default']['username'], $db['default']['password']) or die('Error connecting to mysql');
		$db_selected = mysqli_select_db($conn, $db['default']['database']);
		if (!$db_selected) {
			die ('Can\'t use database : ' . mysql_error());
		}	
		return $conn;
	}

    $conn = connect_database();


    $serial_number  =  $_POST['serial_number'];
    $book_title  =  $_POST['book_title'];
    $book_type  =  $_POST['book_type'];
    $publisher_name  =  $_POST['publisher_name'];
    $date_publisher  =  $_POST['date_publisher'];
    $age_publisher  =  $_POST['age_publisher'];
    $page_number  =  $_POST['page_number'];


    if( isset($_POST['serial_number']) &&  $serial_number!='' )
    {

    $book_data_insert = "  INSERT INTO `all_books`( `serial_number`, `book_title`, `book_type`, `publisher_name`, `date_publisher`, `age_publisher`, `page_number`) VALUES 
    ('".$serial_number."',
     '".$book_title."',
     '".$book_type."',
     '".$publisher_name."',
     '".$date_publisher."',
     '".$age_publisher."',
     '".$page_number."'
     ) ";

     $result_insert = mysqli_query($conn,$book_data_insert);
     echo "<script>alert('Successful...'); </script>";


    }//if data exist

     else{

        echo "<script>alert('Please fill up all fields...'); window.location = history.back();</script>";
	    exit(-1);

     }


?>