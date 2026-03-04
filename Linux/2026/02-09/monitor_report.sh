#!/bin/bash
cur_dir=$(pwd)
log_dir=${cur_dir}/logs

# 统计总行数
function count_total_lines() {
    total_lines=$(wc -l ${log_dir}/access.log | awk '{ print $1 }')
    echo "Total Lines: ${total_lines}"
    echo
}

# 统计状态类型，并输出各个状态类型的出现次数表格
function count_response_status() {
    response_status=$(cat ${log_dir}/access.log | awk '{ print $9 }' | sort | uniq -c | sort -nr)

    echo "Response Status Count:"
    echo "----------------------------------------"
    printf "%-10s | %-10s\n" "Count" "Status"
    echo "----------------------------------------"
    echo "${response_status}" | awk '{ printf "%-10s %-10s\n", $1, $2 }'
    echo
    
}

# 统计IP访问次数
function count_ip_visits() {
    ip_visits=$(cat ${log_dir}/access.log | awk '{ print $1 }' | sort | uniq -c | sort -nr | head -n 3)

    echo "IP Visit Count:"
    echo "----------------------------------------"
    printf "%-10s | %-10s\n" "Count" "IP"
    echo "----------------------------------------"
    echo "${ip_visits}" | awk '{ printf "%-10s %-10s\n", $1, $2 }'
    echo
    
}

function main() {
    count_total_lines
    count_response_status
    count_ip_visits
}
main
