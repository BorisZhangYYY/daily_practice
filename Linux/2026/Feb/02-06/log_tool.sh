#!/bin/bash
cur_dir=$(pwd)
log_dir=${cur_dir}/tmp/test_logs
archive_dir=${cur_dir}/tmp/archive_logs
keep_days=7 # default config

function log_record() {
    echo "[$(date +%Y-%m-%d\ %H:%M:%S)] ${1}" >> ${cur_dir}/log_tool.log
}

function show_disk_usage() {
    disk_info=$(du -h "${log_dir}")
    disk_used=$(echo "${disk_info}" | awk '{ print $1 }')
    echo "Disk Used: ${disk_used}"
    log_record "Disk Used: ${disk_used}"
}

function permission_test() {
    if [ ! -w "${log_dir}" ]; then
        echo "Error: No write permission for ${log_dir}"
        log_record "Error: No write permission for ${log_dir}"
        return 1
    fi
    if [ ! -w "${archive_dir}" ]; then
        echo "Error: No write permission for ${archive_dir}"
        log_record "Error: No write permission for ${archive_dir}"
        return 1
    fi
    echo "Permission test passed"
    log_record "Permission test passed"
}

function dir_exist_test() {
    if [ ! -d "${log_dir}" ]; then
        echo "Error: ${log_dir} does not exist"
        log_record "Error: ${log_dir} does not exist"
        return 1
    fi
    if [ ! -d "${archive_dir}" ]; then
        echo "Error: ${archive_dir} does not exist"
        log_record "Error: ${archive_dir} does not exist"
        return 1
    fi
    echo "Directory test passed"
    log_record "Directory test passed"
}

function tar_archive() {
    permission_test
    if [ $? -ne 0 ]; then
        return 1
    fi
    dir_exist_test
    if [ $? -ne 0 ]; then
        return 1
    fi

    cd "${log_dir}" || return 1

    # 使用临时文件存储待归档文件列表
    local tmp_list="${cur_dir}/tmp/archive_list.txt"
    find . -name "*.log" -mtime +${keep_days} > "${tmp_list}"

    # 统计数量
    local log_count=$(wc -l < "${tmp_list}" | xargs)

    if [ "${log_count}" -eq "0" ]; then
        echo "No logs found to archive (older than ${keep_days} days)."
        log_record "No logs found to archive."
        rm -f "${tmp_list}"
        cd "${cur_dir}"
        return 0
    fi

    echo "Found ${log_count} logs to archive..."

    local archive_name="archive_$(date +%Y%m%d).tar.gz"
    tar -czf "${archive_dir}/${archive_name}" -T "${tmp_list}"

    if [ $? -eq 0 ]; then
        xargs -I {} mv {} "${archive_dir}" < "${tmp_list}"
        
        echo "Archive and move completed, ${log_count} logs archived and moved"
        log_record "Archive and move completed, ${log_count} logs archived and moved"
    else
        echo "Archive failed!"
        log_record "Archive failed!"
    fi

    # 清理
    rm -f "${tmp_list}"
    cd "${cur_dir}"
}

function del_archive() {
    old_tar=$(find "${archive_dir}" -name "archive_*.tar.gz" -mtime +30)
    if [ -z "$old_tar" ]; then
        echo "No archives older than 30 days found."
        log_record "No archives older than 30 days found."
        return 0
    fi

    echo "Delete archives older than 30 days completed"
    log_record "Delete archives older than 30 days completed"
}

function set_new_config() {
    read -p "Enter new config (keep_days): " new_config
    keep_days=$(echo ${new_config} | awk '{ print $1 }')
    echo  "New config is set: keep_days=${keep_days}"
    log_record "New config is set: keep_days=${keep_days}"
}

function quit_script() {
    log_record "Exit log_tool"
    exit 0
}

function menu() {
    echo "################################"
    echo "1. Show Disk Usage"
    echo "2. Tar Archive"
    echo "3. Delete Archives"
    echo "4. Set New Config"
    echo "5. Show Config"
    echo "6. Exit"
    echo "################################"
    echo ""
}

function menu_choose() {
    read -p "Enter your choice:" choice
    if [ -z ${choice} ]; then
        log_record "Error: choice is empty"
        return 1
    fi
    case ${choice} in
        1) show_disk_usage ;;
        2) tar_archive ;;
        3) del_archive ;;
        4) set_new_config ;;
        5) echo "Current config: keep_days=${keep_days}" ;;
        6) quit_script ;;
        *) 
        echo "Error: Invalid choice ${choice}"
        log_record " Error: Invalid choice ${choice}" ;; 
    esac
}

function main() {
    log_record "Start log_tool"
    menu
    menu_choose
}

# 入口函数
while true; do
    main
done
