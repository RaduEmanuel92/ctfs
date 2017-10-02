if [ -z ${1+x} ]; then
	echo "Use: insert_png_header <png_file> <optional_save_path>"
	echo -e "\nIf the optonal save path is not specified the new file will be called:\n\t new.png"
	exit
fi

if [ -z ${2+x} ]; then
	new_file="new.png"
else
	new_file="$2"
fi

python -c 'print chr(137)+chr(80)+chr(78)+chr(71)+chr(13)+chr(10)+chr(26)+chr(10)' | cat - $1 > "$new_file"
