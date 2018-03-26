<?php
    $start_time =microtime(true);
    $data =array();
    for($i=0; $i<3000; $i++)
    {
        array_push($data,rand(0,10000));
    }
//    var_dump($data);
    $temp;
    for($i=0;$i<count($data);$i++)
    {
        for($j=0;$j<count($data)-1-$i;$j++)
        {
            if($data[$j] > $data[$j+1])
            {
                $temp = $data[$j];
                $data[$j] = $data[$j+1];
                $data[$j+1] = $temp;
            }
        }
    }
//    var_dump($data);
    $end_time =microtime(true);
    $time = $end_time-$start_time;
    echo "use time:" ,$time;
