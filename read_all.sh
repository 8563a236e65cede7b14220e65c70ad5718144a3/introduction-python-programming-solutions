for i in $(find . | grep -v "\.idea" | grep -v "\.git" | grep "[.][py|txt]" | sort); do echo -e "\n\n$(printf '*%.0s' {1..100})\n$i\n$(printf '*%.0s' {1..100})" >> ../all.txt; cat $i >> ../all.txt; done