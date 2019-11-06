import sys
import os
import time

test_tool_ver = "1.0.0.2"


# TODO: User Settings -start
driver_ver = 'v2'                       # you need to check phone's driver version
dev_event_name = 'hxmax-touchscreen'    # getevent to check this device name

# common
path_debug = '/proc/android_touch/debug'
path_vendor = '/proc/android_touch/vendor'
path_self_test = '/proc/android_touch/self_test'

# v1
path1_reset = '/proc/android_touch/reset'
path1_inten = '/proc/android_touch/int_en'
path1_senseonoff = '/proc/android_touch/SenseOnOff'
path1_attn = '/proc/android_touch/attn'
path1_register = '/proc/android_touch/register'
path1_crc_test = '/proc/android_touch/CRC_test'
path1_diag = '/proc/android_touch/diag'

# v2
path2_stack = '/proc/android_touch/diag/stack'
path2_delta_s = '/proc/android_touch/diag/delta_s'
path2_dc_s = '/proc/android_touch/diag/dc_s'
path2_baseline_s = '/proc/android_touch/diag/baseline_s'
# TODO: User Settings -end


if driver_ver != 'v2':
    flag_common_v2 = False

    echo_1_rest = 'adb shell "echo 1 > %s"' % path1_reset
    echo_2_rest = 'adb shell "echo 2 > %s"' % path1_reset
    echo_3_rest = 'adb shell "echo 3 > %s"' % path1_reset
    echo_4_rest = 'adb shell "echo 4 > %s"' % path1_reset
    echo_0_inten = 'adb shell "echo 0 > %s"' % path1_inten
    echo_1_inten = 'adb shell "echo 1 > %s"' % path1_inten
    echo_0_senseonoff = 'adb shell "echo 0 > %s"' % path1_senseonoff
    echo_1_senseonoff = 'adb shell "echo 1 > %s"' % path1_senseonoff
    cat_attn = 'adb shell "cat %s"' % path1_attn
    echo_i2c = 'adb shell "echo i > %s"' % path_debug
    echo_int = 'adb shell "echo n > %s"' % path_debug
    echo_register = 'adb shell "echo r:x900000d0 > %s"' % path1_register
    cat_register = 'adb shell "cat %s"' % path1_register
    cat_crc_test = 'adb shell "cat %s"' % path1_crc_test

    echo_diag_0_test = 'adb shell "echo 0 > %s"' % path1_diag
    echo_diag_1_test = 'adb shell "echo 1 > %s"' % path1_diag
    echo_diag_2_test = 'adb shell "echo 2 > %s"' % path1_diag
    echo_diag_11_test = 'adb shell "echo 11 > %s"' % path1_diag
    echo_diag_12_test = 'adb shell "echo 12 > %s"' % path1_diag
    cat_diag_test = 'adb shell "cat %s"' % path1_diag
else:
    flag_common_v2 = True

    echo_1_rest = 'adb shell "echo reset,1 > %s"' % path_debug
    echo_2_rest = 'adb shell "echo reset,2 > %s"' % path_debug
    echo_3_rest = 'adb shell "echo reset,3 > %s"' % path_debug
    echo_4_rest = 'adb shell "echo reset,4 > %s"' % path_debug
    echo_0_inten = 'adb shell "echo int_en,0 > %s"' % path_debug
    echo_1_inten = 'adb shell "echo int_en,1 > %s"' % path_debug
    echo_0_senseonoff = 'adb shell "echo senseonoff,0 > %s"' % path_debug
    echo_1_senseonoff = 'adb shell "echo senseonoff,1 > %s"' % path_debug
    echo_attn = 'adb shell "echo attn > %s"' % path_debug
    echo_i2c = 'adb shell "echo i2c > %s"' % path_debug
    echo_int = 'adb shell "echo int > %s"' % path_debug
    echo_register = 'adb shell "echo register,r:x900000d0 > %s"' % path_debug
    echo_crc_test = 'adb shell "echo crc_test > %s"' % path_debug

    echo_diag_0_test = 'adb shell "echo diag,0 > %s"' % path_debug
    echo_diag_1_test = 'adb shell "echo diag,1 > %s"' % path_debug
    echo_diag_2_test = 'adb shell "echo diag,2 > %s"' % path_debug
    echo_diag_11_test = 'adb shell "echo diag,11 > %s"' % path_debug
    echo_diag_12_test = 'adb shell "echo diag,12 > %s"' % path_debug
    cat_diag_test = 'adb shell "cat %s"' % path2_stack
    cat_diag_delta_s = 'adb shell "cat %s"' % path2_delta_s
    cat_diag_dc_s = 'adb shell "cat %s"' % path2_dc_s
    cat_diag_baseline_s = 'adb shell "cat %s"' % path2_baseline_s


# TODO: init save log path
path = 'scripts/log_' + time.strftime("%Y%m%d-%H%M%S", time.localtime())
os.mkdir(path)
log_tmp = path + '/log_tmp.txt'
log_debug_node_test = path + '/log_debug_node_test.txt'
raw_data_1 = path + '/raw_data_1.txt'
raw_data_2 = path + '/raw_data_2.txt'
raw_data_11 = path + '/raw_data_11.txt'
raw_data_12 = path + '/raw_data_12.txt'
raw_data_delta_s = path + '/raw_data_delta_s.txt'
raw_data_dc_s = path + '/raw_data_dc_s.txt'
raw_data_baseline_s = path + '/raw_data_baseline_s.txt'
log_raw_out_sel_test = path + '/log_raw_out_sel_test.txt'
log_system_suspend = path + '/log_system_suspend.txt'
log_system_resume = path + '/log_system_resume.txt'
log_reboot_test = path + '/log_reboot_test.txt'
log_self_test = path + '/log_self_test.txt'
log_fw_upgrade = path + '/log_fw_upgrade.txt'


# TODO: get argv
t1 = sys.argv[1]
t2 = sys.argv[2]
t3 = sys.argv[3]
t4 = sys.argv[4]
if t4 == 'y':
    t4_times = sys.argv[8]
t5 = sys.argv[5]
if t5 == 'y':
    t5_times = sys.argv[9]
t6 = sys.argv[6]
if t6 == 'y':
    t6_times = sys.argv[10]
t7 = sys.argv[7]
if t7 == 'y':
    t7_times = sys.argv[11]

# TODO: print argv
# for i in range(len(sys.argv)):
#     print(sys.argv[i])


# TODO: test functions
def debug_node_test():
    node_ret = 0
    cat_debug = 'adb shell "cat %s"' % path_debug

    os.system('adb shell "dmesg -c" > ' + log_tmp)
    ##=======================vendor=======================
    node_pass_word = 'Himax Touch Driver Version'
    node_ret = os.system('adb shell "cat %s"' % path_vendor)
    if node_ret != 0:
        print('[HX_AUTO_TEST]cat vendor node test failed')
        return False
    node_test_result = os.popen('adb shell "cat %s"' % path_vendor).read()
    ## Open file
    fp = open(log_debug_node_test, "a")
    fp.write('vendor node test')
    fp.write(node_test_result)
    # close file
    fp.close()

    counter_ret = node_test_result.count(node_pass_word)
    if counter_ret == 0:
        print('[HX_AUTO_TEST]vendor node return value error')
        return False
    ##=======================reset=======================
    node_ret = os.system(echo_1_rest)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo 1 > reset node test failed')
        return False
    node_ret = os.system(echo_2_rest)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo 2 > reset node test failed')
        return False
    node_ret = os.system(echo_3_rest)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo 3 > reset node test failed')
        return False
    node_ret = os.system(echo_4_rest)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo 4 > reset node test failed')
        return False
    ##=======================int_en=======================
    node_ret = os.system(echo_0_inten)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo 0 > int_en node test failed')
        return False
    node_ret = os.system(echo_1_inten)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo 1 > int_en node test failed')
        return False
    ##=======================Sense_On_Off=======================
    node_ret = os.system(echo_0_senseonoff)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo 0 > senseonoff node test failed')
        return False
    node_ret = os.system(echo_1_senseonoff)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo 1 > senseonoff node test failed')
        return False
    ##=======================attn=======================
    node_pass_word = 'attn'
    if flag_common_v2 == True:
        node_ret = os.system(echo_attn)
        if node_ret != 0:
            print('[HX_AUTO_TEST]echo attn > debug node test failed')
            return False
        node_test_result = os.popen(cat_debug).read()
    else:
        node_test_result = os.popen(cat_attn).read()

    ## Open file
    fp = open(log_debug_node_test, "a")
    fp.write('attn node test')
    fp.write(node_test_result)
    # close file
    fp.close()

    counter_ret = node_test_result.count(node_pass_word)
    if counter_ret == 0:
        print('[HX_AUTO_TEST]attn node return value error')
        return False
    ##=======================version=======================
    node_pass_word = 'Himax Touch Driver Version'
    node_ret = os.system('adb shell "echo v > %s"' % path_debug)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo v > debug node test failed')
        return False
    node_test_result = os.popen(cat_debug).read()
    ## Open file
    fp = open(log_debug_node_test, "a")
    fp.write('echo v > debug node test')
    fp.write(node_test_result)
    # close file
    fp.close()

    counter_ret = node_test_result.count(node_pass_word)
    if counter_ret == 0:
        print('[HX_AUTO_TEST]echo v > debug node return value error')
        return False
    ##=======================chip info=======================
    node_pass_word = 'Himax Touch IC Information'
    node_ret = os.system('adb shell "echo d > %s"' % path_debug)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo d > debug node test failed')
        return False
    node_test_result = os.popen(cat_debug).read()
    ## Open file
    fp = open(log_debug_node_test, "a")
    fp.write('echo d > debug node test')
    fp.write(node_test_result)
    # close file
    fp.close()

    counter_ret = node_test_result.count(node_pass_word)
    if counter_ret == 0:
        print('[HX_AUTO_TEST]echo d > debug node return value error')
        return False
    ##=======================i2c status=======================
    node_pass_word = 'I2C communication is good'
    node_ret = os.system(echo_i2c)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo i2c > debug node test failed')
        return False
    node_test_result = os.popen(cat_debug).read()

    ## Open file
    fp = open(log_debug_node_test, "a")
    fp.write('echo i2c > debug node test')
    fp.write(node_test_result)
    # close file
    fp.close()

    counter_ret = node_test_result.count(node_pass_word)
    if counter_ret == 0:
        print('[HX_AUTO_TEST]echo i2c > debug node return value error')
        return False
    ##=======================int register=======================
    node_pass_word = 'Driver register Interrupt'
    node_ret = os.system(echo_int)
    if node_ret != 0:
        print('[HX_AUTO_TEST]echo int > debug node test failed')
        return False
    node_test_result = os.popen(cat_debug).read()
    ## Open file
    fp = open(log_debug_node_test, "a")
    fp.write('echo int > debug node test')
    fp.write(node_test_result)
    # close file
    fp.close()

    counter_ret = node_test_result.count(node_pass_word)
    if counter_ret == 0:
        print('[HX_AUTO_TEST]echo int > debug node return value error')
        return False
    ##=======================register read test=======================
    node_pass_word = '0x83'
    node_ret = os.system(echo_register)
    if node_ret != 0:
        print('[HX_AUTO_TEST]register read node test failed')
        return False
    if flag_common_v2 == True:
        node_test_result = os.popen(cat_debug).read()
    else:
        node_test_result = os.popen(cat_register).read()
    ## Open file
    fp = open(log_debug_node_test, "a")
    fp.write('0x900000d0 register read node test')
    fp.write(node_test_result)
    # close file
    fp.close()

    counter_ret = node_test_result.count(node_pass_word)
    if counter_ret == 0:
        print('[HX_AUTO_TEST]register read node return value error')
        return False
    ##=======================flash crc test=======================
    node_pass_word = 'CRC test is Pass'
    if flag_common_v2 == True:
        node_ret = os.system(echo_crc_test)
        if node_ret != 0:
            print('[HX_AUTO_TEST]echo crc_test > debug node test failed')
            return False
        node_test_result = os.popen(cat_debug).read()
    else:
        node_test_result = os.popen(cat_crc_test).read()
    ## Open file
    fp = open(log_debug_node_test, "a")
    fp.write('echo crc_test > debug node test')
    fp.write(node_test_result)
    # close file
    fp.close()

    counter_ret = node_test_result.count(node_pass_word)
    if counter_ret == 0:
        print('[HX_AUTO_TEST]echo crc_test > debug node return value error')
        return False

    return True


def raw_out_sel_test():
    i2c_header = 'i2c'
    error_msg = 'error'
    timeout_msg = 'timeout'
    counter_h = 0
    counter_e1 = 0
    counter_e2 = 0

    os.system('adb shell "dmesg -c" > ' + log_tmp)
    ##============= diag=1 test =========================##
    os.system(echo_diag_1_test)
    get_event_result = os.popen(cat_diag_test).read()

    # print(get_event_result)
    ## Open file
    fp = open(raw_data_1, "a")
    fp.write(get_event_result)
    # close file
    fp.close()
    os.system('adb shell "dmesg -c" > ' + log_raw_out_sel_test)
    counter_h = get_event_result.count(i2c_header)
    if counter_h != 0:
        counter_e1 = get_event_result.count(error_msg)
        counter_e2 = get_event_result.count(timeout_msg)
        if counter_e1 != 0 or counter_e2 != 0:
            print('[HX_AUTO_TEST]set diag=1 test failed')
            return False

    ##============= diag=2 test =========================##
    os.system(echo_diag_2_test)
    get_event_result = os.popen(cat_diag_test).read()

    # print(get_event_result)
    ## Open file
    fp = open(raw_data_2, "a")
    fp.write(get_event_result)
    # close file
    fp.close()
    os.system('adb shell "dmesg -c" > ' + log_raw_out_sel_test)
    counter_h = get_event_result.count(i2c_header)
    if counter_h != 0:
        counter_e1 = get_event_result.count(error_msg)
        counter_e2 = get_event_result.count(timeout_msg)
        if counter_e1 != 0 or counter_e2 != 0:
            print('[HX_AUTO_TEST]set diag=2 test failed')
            return False

    # ============= diag=11 test =========================
    os.system(echo_diag_11_test)
    get_event_result = os.popen(cat_diag_test).read()

    # print(get_event_result)
    ## Open file
    fp = open(raw_data_11, "a")
    fp.write(get_event_result)
    # close file
    fp.close()
    os.system('adb shell "dmesg -c" > ' + log_raw_out_sel_test)
    counter_h = get_event_result.count(i2c_header)
    if counter_h != 0:
        counter_e1 = get_event_result.count(error_msg)
        counter_e2 = get_event_result.count(timeout_msg)
        if counter_e1 != 0 or counter_e2 != 0:
            print('[HX_AUTO_TEST]set diag=11 test failed')
            return False

    ##============= diag=12 test =========================##
    os.system(echo_diag_12_test)
    get_event_result = os.popen(cat_diag_test).read()

    # print(get_event_result)
    ## Open file
    fp = open(raw_data_12, "a")
    fp.write(get_event_result)
    # close file
    fp.close()
    os.system('adb shell "dmesg -c" > ' + log_raw_out_sel_test)
    counter_h = get_event_result.count(i2c_header)
    if counter_h != 0:
        counter_e1 = get_event_result.count(error_msg)
        counter_e2 = get_event_result.count(timeout_msg)
        if counter_e1 != 0 or counter_e2 != 0:
            print('[HX_AUTO_TEST]set diag=12 test failed')
            return False

    ##============= delta_s test =========================##
    if flag_common_v2 == True:
        ## for Common V2 driver
        get_event_result = os.popen(cat_diag_delta_s).read()

        # print(get_event_result)
        ## Open file
        fp = open(raw_data_delta_s, "a")
        fp.write(get_event_result)
        # close file
        fp.close()
        os.system('adb shell "dmesg -c" > ' + log_raw_out_sel_test)
        counter_h = get_event_result.count(i2c_header)
        if counter_h != 0:
            counter_e1 = get_event_result.count(error_msg)
            counter_e2 = get_event_result.count(timeout_msg)
            if counter_e1 != 0 or counter_e2 != 0:
                print('[HX_AUTO_TEST]set delta_s test failed')
                return False

    ##============= dc_s test =========================##
    if flag_common_v2 == True:
        ## for Common V2 driver
        get_event_result = os.popen(cat_diag_dc_s).read()

        # print(get_event_result)
        ## Open file
        fp = open(raw_data_dc_s, "a")
        fp.write(get_event_result)
        # close file
        fp.close()
        os.system('adb shell "dmesg -c" > ' + log_raw_out_sel_test)
        counter_h = get_event_result.count(i2c_header)
        if counter_h != 0:
            counter_e1 = get_event_result.count(error_msg)
            counter_e2 = get_event_result.count(timeout_msg)
            if counter_e1 != 0 or counter_e2 != 0:
                print('[HX_AUTO_TEST]set dc_s test failed')
                return False

    ##============= baseline_s test =========================##
    if flag_common_v2 == True:
        ## for Common V2 driver
        get_event_result = os.popen(cat_diag_baseline_s).read()

        # print(get_event_result)
        ## Open file
        fp = open(raw_data_baseline_s, "a")
        fp.write(get_event_result)
        # close file
        fp.close()
        os.system('adb shell "dmesg -c" > ' + log_raw_out_sel_test)
        counter_h = get_event_result.count(i2c_header)
        if counter_h != 0:
            counter_e1 = get_event_result.count(error_msg)
            counter_e2 = get_event_result.count(timeout_msg)
            if counter_e1 != 0 or counter_e2 != 0:
                print('[HX_AUTO_TEST]set baseline_s test failed')
                return False

    ##============= diag=0 close =========================##
    os.system(echo_diag_0_test)
    get_event_result = os.popen(cat_diag_test).read()

    os.system('adb shell "dmesg -c" > ' + log_raw_out_sel_test)
    counter_h = get_event_result.count(i2c_header)
    if counter_h != 0:
        counter_e1 = get_event_result.count(error_msg)
        counter_e2 = get_event_result.count(timeout_msg)
        if counter_e1 != 0 or counter_e2 != 0:
            print('[HX_AUTO_TEST]set diag=0 test failed')
            return False

    return True


def system_init():
    node_ret = os.system('adb root')
    if node_ret != 0:
        print('[HX_AUTO_TEST]device NOT Found')
        return False
    os.system('adb remount')
    os.system('adb shell "setenforce 0"')
    os.system('adb shell "input keyevent 82"')
    os.system('adb shell "input keyevent 82"')

    return True


def suspend_resume_test(times):
    os.system('adb shell "dmesg -c" > ' + log_tmp)

    for i in range(0, int(times), 1):
        print('[HX_AUTO_TEST]test times', i + 1, 'Total', times)
        os.system('adb shell "input keyevent 26"')
        time.sleep(1)
        os.system('adb shell "dmesg -c | grep HXTP" > ' + log_system_suspend)
        os.system('adb shell "input keyevent 26"')
        os.system('adb shell "input keyevent 82"')
        time.sleep(1)
        os.system('adb shell "dmesg -c | grep HXTP" > ' + log_system_resume)

        # =================suspend test item=====================
        suspend_key_word = 'himax_chip_common_suspend'
        ## Open file
        fp = open(log_system_suspend, "r")
        lines = fp.readlines()
        # close file
        fp.close()

        counter = 0
        counter_2 = 0
        # print content
        for i in range(len(lines)):
            strtmp = lines[i].rstrip()
            # print (strtmp)
            counter = strtmp.count(suspend_key_word)
            counter_2 += counter

        # print(counter_2)
        if counter_2 != 2:
            print('[HX_AUTO_TEST]Suspend function has problem')
            return False

        # =================resume test item=====================
        resume_key_word = 'himax_chip_common_resume'
        ## Open file
        fp = open(log_system_resume, "r")
        lines = fp.readlines()
        # close file
        fp.close()

        counter = 0
        counter_2 = 0
        # print content
        for i in range(len(lines)):
            strtmp = lines[i].rstrip()
            # print (strtmp)
            counter = strtmp.count(resume_key_word)
            counter_2 += counter

        # print(counter_2)
        if counter_2 != 2:
            print('[HX_AUTO_TEST]Resume function has problem')
            return False

    return True


def reboot_test(times):
    for i in range(0, int(times), 1):
        print('[HX_AUTO_TEST]test times', i + 1, 'Total', times)
        os.system('adb shell reboot')
        time.sleep(10)
        os.system('adb wait-for-device')
        os.system('adb shell "dmesg -c | grep HXTP" > ' + log_reboot_test)

        # =================reboot test item=====================
        error_key_word = 'error'
        failed_key_word = 'fail'
        passd_key_word = 'himax_int_register_trigger'

        exp_error_word = 'prepare kp_getname_kernel failed'

        # Open file
        fp = open(log_reboot_test, "r")
        lines = fp.readlines()
        # close file
        fp.close()

        counter = 0
        error_counter = 0
        pass_counter = 0
        # print content
        for i in range(len(lines)):
            strtmp = lines[i].rstrip()
            # print (strtmp)
            counter = strtmp.count(error_key_word)
            error_counter += counter
            counter = strtmp.count(failed_key_word)
            if strtmp.count(exp_error_word) == 0:
                error_counter += counter

            counter = strtmp.count(passd_key_word)
            pass_counter += counter

        print('[HX_AUTO_TEST]fail_log', error_counter)
        print('[HX_AUTO_TEST]pass_log', pass_counter)
        if error_counter != 0 or pass_counter == 0:
            print('[HX_AUTO_TEST]Driver probe has problem')
            return False

    return True


def inspection_test(times):
    if os.path.isfile("hx_criteria_pass.csv") and os.path.isfile("hx_criteria_fail.csv"):
        print("hx_criteria_pass.csv,hx_criteria_fail.csv check ok")
    else:
        print("Please put hx_criteria_pass.csv,hx_criteria_fail.csv")
        return False

    os.system('adb shell "dmesg -c" > ' + log_tmp)

    for i in range(0, int(times), 1):
        print('[HX_AUTO_TEST]test times', i, 'Total', times)
        # =================himax_self test pass case=====================
        os.system('adb push hx_criteria_pass.csv /system/etc/firmware/hx_criteria.csv')
        # time.sleep(5)
        self_test_result = os.popen('adb shell "cat %s"' % path_self_test).read()
        os.system('adb shell "dmesg -c | grep HXTP" > ' + log_self_test)
        print('self_test_result', self_test_result)

        self_test_pass = 'Pass'
        counter = 0

        counter = self_test_result.count(self_test_pass)
        # print(counter)
        if counter == 0:
            print('[HX_AUTO_TEST]himax_self test pass case failed')
            return False
        # =================himax_self test pass case=====================
        # =================himax_self test fail case=====================
        os.system('adb push hx_criteria_fail.csv /system/etc/firmware/hx_criteria.csv')
        # time.sleep(5)
        self_test_result = os.popen('adb shell "cat %s"' % path_self_test).read()
        os.system('adb shell "dmesg -c | grep HXTP" > ' + log_self_test)
        print('self_test_result', self_test_result)

        self_test_fail = 'Fail'
        counter = 0

        counter = self_test_result.count(self_test_fail)
        # print(counter)
        if counter == 0:
            print('[HX_AUTO_TEST]himax_self test fail case failed')
            return False
        # =================himax_self test fail case=====================
    return True


def fw_upgrade_test(times):
    if os.path.isfile("himax_firmware_1.bin") and os.path.isfile("himax_firmware_2.bin"):
        print("himax_firmware_1.bin,himax_firmware_2.bin check ok")
    else:
        print("Please put himax_firmware_1.bin,himax_firmware_2.bin into folder")
        return False

    os.system('adb shell "dmesg -c" > ' + log_tmp)

    for i in range(0, int(times), 1):
        print('[HX_AUTO_TEST]test times', i, 'Total', times)
        # =================himax_firmware test 1st time=====================
        os.system('adb push himax_firmware_1.bin /system/etc/firmware/himax_firmware.bin')
        os.system('adb shell "echo t "himax_firmware.bin" > %s' % path_debug)
        # time.sleep(5)
        fw_upgrade_result = os.popen('adb shell "cat %s"' % path_debug).read()
        os.system('adb shell "dmesg -c | grep HXTP" > ' + log_fw_upgrade)
        print('fw_upgrade_result', fw_upgrade_result)

        fw_upgrade_pass = 'FW Update Complete'
        counter = 0

        counter = fw_upgrade_result.count(fw_upgrade_pass)
        # print(counter)
        if counter == 0:
            print('[HX_AUTO_TEST]1st firmware test failed')
            return False
        # =================himax_firmware test 1st time=====================
        # =================himax_firmware test 2nd time=====================
        os.system('adb push himax_firmware_2.bin /system/etc/firmware/himax_firmware.bin')
        os.system('adb shell "echo t "himax_firmware.bin" > %s' % path_debug)
        # time.sleep(5)
        fw_upgrade_result = os.popen('adb shell "cat %s"' % path_debug).read()
        os.system('adb shell "dmesg -c | grep HXTP" > ' + log_fw_upgrade)
        print('fw_upgrade_result', fw_upgrade_result)

        counter = 0

        counter = fw_upgrade_result.count(fw_upgrade_pass)
        # print(counter)
        if counter == 0:
            print('[HX_AUTO_TEST]2nd firmware test failed')
            return False
        # =================himax_firmware test 2nd time=====================
    return True


def check_input_register():
    get_event_result = os.popen('adb shell "getevent -i | grep touchscreen"').read()
    counter = get_event_result.count(dev_event_name)
    if counter == 0:
        print('[HX_AUTO_TEST]Input device register failed')
        return False

    return True


def print_status():
    header = "[HX_AUTO_TEST]Test Result:"
    if init_ret:
        init_s = "[init]=P ,"
    else:
        init_s = "[init]=F ,"

    if t1 == 'y':
        if t1_ret:
            t1_s = "[t1]=P ,"
        else:
            t1_s = "[t1]=F ,"
    else:
        t1_s = "[t1]=N ,"

    if t2 == 'y':
        if t2_ret:
            t2_s = "[t2]=P ,"
        else:
            t2_s = "[t2]=F ,"
    else:
        t2_s = "[t2]=N ,"

    if t3 == 'y':
        if t3_ret:
            t3_s = "[t3]=P ,"
        else:
            t3_s = "[t3]=F ,"
    else:
        t3_s = "[t3]=N ,"

    if t4 == 'y':
        if t4_ret:
            t4_s = "[t4]=P ,"
        else:
            t4_s = "[t4]=F ,"
    else:
        t4_s = "[t4]=N ,"

    if t5 == 'y':
        if t5_ret:
            t5_s = "[t5]=P ,"
        else:
            t5_s = "[t5]=F ,"
    else:
        t5_s = "[t5]=N ,"

    if t6 == 'y':
        if t6_ret:
            t6_s = "[t6]=P ,"
        else:
            t6_s = "[t6]=F ,"
    else:
        t6_s = "[t6]=N ,"

    if t7 == 'y':
        if t7_ret:
            t7_s = "[t7]=P"
        else:
            t7_s = "[t7]=F"
    else:
        t7_s = "[t7]=N"
    total_s = header + init_s + t1_s + t2_s + t3_s + t4_s + t5_s + t6_s + t7_s
    print(total_s)


# TODO: start to run this script
t1_ret = False
t2_ret = False
t3_ret = False
t4_ret = False
t5_ret = False
t6_ret = False
t7_ret = False

print('[HX_AUTO_TEST] Tool Version ' + test_tool_ver)

init_ret = system_init()

if init_ret:
    print('[HX_AUTO_TEST]System initial Pass!')
else:
    print('[HX_AUTO_TEST]Test Result:[init]=F ,[t1]=N ,[t2]=N ,[t3]=N ,[t4]=N ,[t5]=N ,[t6]=N ,[t7]=N')
    sys.exit('[HX_AUTO_TEST]System initial Fail!')


# TODO: function 1 test
if t1 == 'y':
    t1_ret = check_input_register()
    if t1_ret:
        print('[HX_AUTO_TEST]Check Input Register Test Pass!')
    else:
        print_status()
        sys.exit('[HX_AUTO_TEST]Check Input Register Test Fail!')

# TODO: function 2 test
if t2 == 'y':
    t2_ret = debug_node_test()
    if t2_ret:
        print('[HX_AUTO_TEST]Debug file node Test Pass!')
    else:
        print_status()
        sys.exit('[HX_AUTO_TEST]Debug file node Test Fail!')

# TODO: function 3 test
if t3 == 'y':
    t3_ret = raw_out_sel_test()
    if t3_ret:
        print('[HX_AUTO_TEST]Raw data out Test Pass!')
    else:
        print_status()
        sys.exit('[HX_AUTO_TEST]Raw data out Test Fail!')

# TODO: function 4 test
if t4 == 'y':
    t4_ret = inspection_test(t4_times)
    if t4_ret:
        print('[HX_AUTO_TEST]Inspection Test Pass!')
    else:
        print_status()
        sys.exit('[HX_AUTO_TEST]Inspection Test Fail!')

# TODO: function 5 test
if t5 == 'y':
    t5_ret = fw_upgrade_test(t5_times)
    if t5_ret:
        print('[HX_AUTO_TEST]FW upgrade Test Pass!')
    else:
        print_status()
        sys.exit('[HX_AUTO_TEST]FW upgrade Test Fail!')

# TODO: function 6 test
if t6 == 'y':
    t6_ret = suspend_resume_test(t6_times)
    if t6_ret:
        print('[HX_AUTO_TEST]Suspend Resume Test Pass!')
    else:
        print_status()
        sys.exit('[HX_AUTO_TEST]Suspend Resume Test Fail!')

# TODO: function 7 test
if t7 == 'y':
    t7_ret = reboot_test(t7_times)
    if t7_ret:
        print('[HX_AUTO_TEST]Reboot Test Pass!')
    else:
        print_status()
        sys.exit('[HX_AUTO_TEST]Reboot Test Fail!')

print_status()


