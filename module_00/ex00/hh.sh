#!/bin/sh
curl GET https://api.hh.ru/vacancies -G \
    --data-urlencode "search_field=name" \
    --data-urlencode "text=data scientist" \
    --data-urlencode "per_page=20" \
    | jq > hh.json
