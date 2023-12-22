finch stop $(finch ps -a -q)
finch rm $(finch ps -a -q)

finch system prune
finch compose down -v 

