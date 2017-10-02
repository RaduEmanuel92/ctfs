for a in `cat encodings.list`; do
  printf "$a  "
  iconv -f $a -t UTF-8 conf.bin > /dev/null 2>&1 \
    && echo "ok: $a" || echo "fail: $a"
done | tee result.txt