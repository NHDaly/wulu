<?php

	while (1) {
	echo "hi";
	}
		$spawnstring = "bash -c 'exec nohup php addEpToDb.php httpwwwxkcdcomrssxml \"Shake That\" http://xkcd.com/1261/ \"Fri, 06 Sep 2013 04:00:00 -0000\" < /dev/null > /dev/null 2>&1 &'";
		echo $spawnstring;
		exec($spawnstring);

#    # spawning PHP process for text-to-audio conversion
#    #  -- make sure to spawn in seperate process not linked to current page.
#    $spawnString = 'bash -c "exec nohup php addEpToDb.php < /dev/null > /dev/null 2>&1 &"';
#    exec($spawnString);
#    exec($spawnString);
#    exec($spawnString);
#    exec($spawnString);

    echo "HELLO, i'm finished. c:\n";

?>
