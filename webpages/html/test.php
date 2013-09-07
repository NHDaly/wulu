<?php

    # spawning PHP process for text-to-audio conversion
    #  -- make sure to spawn in seperate process not linked to current page.
    $spawnString = 'bash -c "exec nohup php addEpToDb.php < /dev/null > /dev/null 2>&1 &"';
    exec($spawnString);
    exec($spawnString);
    exec($spawnString);
    exec($spawnString);

    echo "HELLO, i'm finished. c:\n";

?>
