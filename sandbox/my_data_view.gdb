define view_my_data
    set $start = 0x00021174
    set $count = 400
    while $count > 0
        printf "0x%x: ", $start
        x/6b $start
        set $start = $start + 6
        set $count = $count - 1
    end
end
document view_my_data
Prints my_data in groups of 6 bytes.
Usage:
  view_my_data
end
