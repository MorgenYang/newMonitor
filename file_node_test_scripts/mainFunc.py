import sys
import os
import time


# TODO: define test functions ---start
flag_common_v2 = True
v1_str = 'v1'


test_tool_ver = "1.0.0.1"

# ============= function initial =============
init_ret = 0
t1_ret = 0
t2_ret = 0
t3_ret = 0
t4_ret = 0
t5_ret = 0
t6_ret = 0
t7_ret = 0

t4_times = ''
t5_times = ''
t6_times = ''
t7_times = ''


print('[HX_AUTO_TEST] Tool Version ' + test_tool_ver)

driver_ver = 'v2'


# debug_node_test
def debug_node_test_node_def(ver):
    global echo_1_rest
    global echo_2_rest
    global echo_3_rest
    global echo_4_rest
    global echo_0_inten
    global echo_1_inten
    global echo_0_senseonoff
    global echo_1_senseonoff
    global echo_attn
    global echo_i2c
    global echo_int
    global echo_register
    global echo_crc_test
    global cat_attn
    global cat_register
    global cat_crc_test

    if ver == v1_str:
        ## for Common V1 driver
        flag_common_v2 = False
        echo_1_rest = 'adb shell "echo 1 > /proc/android_touch/reset"'
        echo_2_rest = 'adb shell "echo 2 > /proc/android_touch/reset"'
        echo_3_rest = 'adb shell "echo 3 > /proc/android_touch/reset"'
        echo_4_rest = 'adb shell "echo 4 > /proc/android_touch/reset"'
        echo_0_inten = 'adb shell "echo 0 > /proc/android_touch/int_en"'
        echo_1_inten = 'adb shell "echo 1 > /proc/android_touch/int_en"'
        echo_0_senseonoff = 'adb shell "echo 0 > /proc/android_touch/SenseOnOff"'
        echo_1_senseonoff = 'adb shell "echo 1 > /proc/android_touch/SenseOnOff"'
        cat_attn = 'adb shell "cat /proc/android_touch/attn"'
        echo_i2c = 'adb shell "echo i > /proc/android_touch/debug"'
        echo_int = 'adb shell "echo n > /proc/android_touch/debug"'
        echo_register = 'adb shell "echo r:x900000d0 > /proc/android_touch/register"'
        cat_register = 'adb shell "cat /proc/android_touch/register"'
        cat_crc_test = 'adb shell "cat /proc/android_touch/CRC_test"'
    else:
        ## for Common V2 driver
        flag_common_v2 = True
        echo_1_rest = 'adb shell "echo reset,1 > /proc/android_touch/debug"'
        echo_2_rest = 'adb shell "echo reset,2 > /proc/android_touch/debug"'
        echo_3_rest = 'adb shell "echo reset,3 > /proc/android_touch/debug"'
        echo_4_rest = 'adb shell "echo reset,4 > /proc/android_touch/debug"'
        echo_0_inten = 'adb shell "echo int_en,0 > /proc/android_touch/debug"'
        echo_1_inten = 'adb shell "echo int_en,1 > /proc/android_touch/debug"'
        echo_0_senseonoff = 'adb shell "echo senseonoff,0 > /proc/android_touch/debug"'
        echo_1_senseonoff = 'adb shell "echo senseonoff,1 > /proc/android_touch/debug"'
        echo_attn = 'adb shell "echo attn > /proc/android_touch/debug"'
        echo_i2c = 'adb shell "echo i2c > /proc/android_touch/debug"'
        echo_int = 'adb shell "echo int > /proc/android_touch/debug"'
        echo_register = 'adb shell "echo register,r:x900000d0 > /proc/android_touch/debug"'
        echo_crc_test = 'adb shell "echo crc_test > /proc/android_touch/debug"'


def debug_node_test():
	node_ret = 0
	cat_debug = 'adb shell "cat /proc/android_touch/debug"'

	os.system('adb shell "dmesg -c" > log_tmp.txt')
	##=======================vendor=======================
	node_pass_word = 'Himax Touch Driver Version'
	node_ret = os.system('adb shell "cat /proc/android_touch/vendor"')
	if node_ret != 0:
		print('[HX_AUTO_TEST]cat vendor node test failed')
		return False
	node_test_result = os.popen('adb shell "cat /proc/android_touch/vendor"').read()
	## Open file
	fp = open('log_debug_node_test.txt', "a")
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
	fp = open('log_debug_node_test.txt', "a")
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
	node_ret = os.system('adb shell "echo v > /proc/android_touch/debug"')
	if node_ret != 0:
		print('[HX_AUTO_TEST]echo v > debug node test failed')
		return False
	node_test_result = os.popen(cat_debug).read()
	## Open file
	fp = open('log_debug_node_test.txt', "a")
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
	node_ret = os.system('adb shell "echo d > /proc/android_touch/debug"')
	if node_ret != 0:
		print('[HX_AUTO_TEST]echo d > debug node test failed')
		return False
	node_test_result = os.popen(cat_debug).read()
	## Open file
	fp = open('log_debug_node_test.txt', "a")
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
	fp = open('log_debug_node_test.txt', "a")
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
	fp = open('log_debug_node_test.txt', "a")
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
	fp = open('log_debug_node_test.txt', "a")
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
	fp = open('log_debug_node_test.txt', "a")
	fp.write('echo crc_test > debug node test')
	fp.write(node_test_result)
	# close file
	fp.close()

	counter_ret = node_test_result.count(node_pass_word)
	if counter_ret == 0:
		print('[HX_AUTO_TEST]echo crc_test > debug node return value error')
		return False

	return True


# raw_out_sel_test
def raw_out_sel_test_node_def(ver):
	global echo_diag_0_test
	global echo_diag_1_test
	global echo_diag_2_test
	global echo_diag_11_test
	global echo_diag_12_test
	global cat_diag_test
	global cat_diag_delta_s
	global cat_diag_dc_s
	global cat_diag_baseline_s

	if ver == v1_str:
		## for Common V1 driver
		flag_common_v2 = False
		echo_diag_0_test = 'adb shell "echo 0 > /proc/android_touch/diag"'
		echo_diag_1_test = 'adb shell "echo 1 > /proc/android_touch/diag"'
		echo_diag_2_test = 'adb shell "echo 2 > /proc/android_touch/diag"'
		echo_diag_11_test = 'adb shell "echo 11 > /proc/android_touch/diag"'
		echo_diag_12_test = 'adb shell "echo 12 > /proc/android_touch/diag"'
		cat_diag_test = 'adb shell "cat /proc/android_touch/diag"'
	else:
		## for Common V2 driver
		flag_common_v2 = True
		echo_diag_0_test = 'adb shell "echo diag,0 > /proc/android_touch/debug"'
		echo_diag_1_test = 'adb shell "echo diag,1 > /proc/android_touch/debug"'
		echo_diag_2_test = 'adb shell "echo diag,2 > /proc/android_touch/debug"'
		echo_diag_11_test = 'adb shell "echo diag,11 > /proc/android_touch/debug"'
		echo_diag_12_test = 'adb shell "echo diag,12 > /proc/android_touch/debug"'
		cat_diag_test = 'adb shell "cat /proc/android_touch/diag/stack"'
		cat_diag_delta_s = 'adb shell "cat /proc/android_touch/diag/delta_s"'
		cat_diag_dc_s = 'adb shell "cat /proc/android_touch/diag/dc_s"'
		cat_diag_baseline_s = 'adb shell "cat /proc/android_touch/diag/baseline_s"'


def raw_out_sel_test():
	i2c_header = 'i2c'
	error_msg = 'error'
	timeout_msg = 'timeout'
	counter_h = 0
	counter_e1 = 0
	counter_e2 = 0

	os.system('adb shell "dmesg -c" > log_tmp.txt')
	##============= diag=1 test =========================##
	os.system(echo_diag_1_test)
	get_event_result = os.popen(cat_diag_test).read()

	# print(get_event_result)
	## Open file
	fp = open('raw_data_1.txt', "a")
	fp.write(get_event_result)
	# close file
	fp.close()
	os.system('adb shell "dmesg -c" > log_raw_out_sel_test.txt')
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
	fp = open('raw_data_2.txt', "a")
	fp.write(get_event_result)
	# close file
	fp.close()
	os.system('adb shell "dmesg -c" > log_raw_out_sel_test.txt')
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
	fp = open('raw_data_11.txt', "a")
	fp.write(get_event_result)
	# close file
	fp.close()
	os.system('adb shell "dmesg -c" > log_raw_out_sel_test.txt')
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
	fp = open('raw_data_12.txt', "a")
	fp.write(get_event_result)
	# close file
	fp.close()
	os.system('adb shell "dmesg -c" > log_raw_out_sel_test.txt')
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
		fp = open('raw_data_delta_s.txt', "a")
		fp.write(get_event_result)
		# close file
		fp.close()
		os.system('adb shell "dmesg -c" > log_raw_out_sel_test.txt')
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
		fp = open('raw_data_dc_s.txt', "a")
		fp.write(get_event_result)
		# close file
		fp.close()
		os.system('adb shell "dmesg -c" > log_raw_out_sel_test.txt')
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
		fp = open('raw_data_baseline_s.txt', "a")
		fp.write(get_event_result)
		# close file
		fp.close()
		os.system('adb shell "dmesg -c" > log_raw_out_sel_test.txt')
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

	os.system('adb shell "dmesg -c" > log_raw_out_sel_test.txt')
	counter_h = get_event_result.count(i2c_header)
	if counter_h != 0:
		counter_e1 = get_event_result.count(error_msg)
		counter_e2 = get_event_result.count(timeout_msg)
		if counter_e1 != 0 or counter_e2 != 0:
			print('[HX_AUTO_TEST]set diag=0 test failed')
			return False

	return True


def print_status():
	header = "[HX_AUTO_TEST]Test Result:"
	if init_ret == True:
		init_s = "[init]=P ,"
	else:
		init_s = "[init]=F ,"

	if t1 == 'y':
		if t1_ret == True:
			t1_s = "[t1]=P ,"
		else:
			t1_s = "[t1]=F ,"
	else:
		t1_s = "[t1]=N ,"

	if t2 == 'y':
		if t2_ret == True:
			t2_s = "[t2]=P ,"
		else:
			t2_s = "[t2]=F ,"
	else:
		t2_s = "[t2]=N ,"

	if t3 == 'y':
		if t3_ret == True:
			t3_s = "[t3]=P ,"
		else:
			t3_s = "[t3]=F ,"
	else:
		t3_s = "[t3]=N ,"

	if t4 == 'y':
		if t4_ret == True:
			t4_s = "[t4]=P ,"
		else:
			t4_s = "[t4]=F ,"
	else:
		t4_s = "[t4]=N ,"

	if t5 == 'y':
		if t5_ret == True:
			t5_s = "[t5]=P ,"
		else:
			t5_s = "[t5]=F ,"
	else:
		t5_s = "[t5]=N ,"

	if t6 == 'y':
		if t6_ret == True:
			t6_s = "[t6]=P ,"
		else:
			t6_s = "[t6]=F ,"
	else:
		t6_s = "[t6]=N ,"

	if t7 == 'y':
		if t7_ret == True:
			t7_s = "[t7]=P"
		else:
			t7_s = "[t7]=F"
	else:
		t7_s = "[t7]=N"
	total_s = header + init_s + t1_s + t2_s + t3_s + t4_s + t5_s + t6_s + t7_s
	print(total_s)


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
	os.system('adb shell "dmesg -c" > log_tmp.txt')

	for i in range(0, int(times), 1):
		print('[HX_AUTO_TEST]test times', i + 1, 'Total', times)
		os.system('adb shell "input keyevent 26"')
		time.sleep(1)
		os.system('adb shell "dmesg -c | grep HXTP" > log_system_suspend.txt')
		os.system('adb shell "input keyevent 26"')
		os.system('adb shell "input keyevent 82"')
		time.sleep(1)
		os.system('adb shell "dmesg -c | grep HXTP" > log_system_resume.txt')

		# =================suspend test item=====================
		suspend_key_word = 'himax_chip_common_suspend'
		## Open file
		fp = open('log_system_suspend.txt', "r")
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
		fp = open('log_system_resume.txt', "r")
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
		os.system('adb shell "dmesg -c | grep HXTP" > log_reboot_test.txt')

		# =================reboot test item=====================
		error_key_word = 'error'
		failed_key_word = 'fail'
		passd_key_word = 'himax_int_register_trigger'

		exp_error_word = 'prepare kp_getname_kernel failed'

		# Open file
		fp = open('log_reboot_test.txt', "r")
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

	os.system('adb shell "dmesg -c" > log_tmp.txt')

	for i in range(0, int(times), 1):
		print('[HX_AUTO_TEST]test times', i, 'Total', times)
		# =================himax_self test pass case=====================
		os.system('adb push hx_criteria_pass.csv /system/etc/firmware/hx_criteria.csv')
		# time.sleep(5)
		self_test_result = os.popen('adb shell "cat /proc/android_touch/self_test"').read()
		os.system('adb shell "dmesg -c | grep HXTP" > log_self_test.txt')
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
		self_test_result = os.popen('adb shell "cat /proc/android_touch/self_test"').read()
		os.system('adb shell "dmesg -c | grep HXTP" > log_self_test.txt')
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

	os.system('adb shell "dmesg -c" > log_tmp.txt')

	for i in range(0, int(times), 1):
		print('[HX_AUTO_TEST]test times', i, 'Total', times)
		# =================himax_firmware test 1st time=====================
		os.system('adb push himax_firmware_1.bin /system/etc/firmware/himax_firmware.bin')
		os.system('adb shell "echo t "himax_firmware.bin" > /proc/android_touch/debug')
		# time.sleep(5)
		fw_upgrade_result = os.popen('adb shell "cat /proc/android_touch/debug"').read()
		os.system('adb shell "dmesg -c | grep HXTP" > log_fw_upgrade.txt')
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
		os.system('adb shell "echo t "himax_firmware.bin" > /proc/android_touch/debug')
		# time.sleep(5)
		fw_upgrade_result = os.popen('adb shell "cat /proc/android_touch/debug"').read()
		os.system('adb shell "dmesg -c | grep HXTP" > log_fw_upgrade.txt')
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
    # get_event_pass='sec_touchscreen'
    get_event_pass='hxmax-touchscreen'
    # get_event_pass='mtk-tpd'
    counter = 0

    get_event_result = os.popen('adb shell "getevent -i | grep touchscreen"').read()
    counter = get_event_result.count(get_event_pass)
    if counter == 0:
        print('[HX_AUTO_TEST]Input device register failed')
        return False

    return True


init_ret = system_init()
if init_ret == True:
	print('[HX_AUTO_TEST]System initial Pass!')
else:
	print('[HX_AUTO_TEST]Test Result:[init]=F ,[t1]=N ,[t2]=N ,[t3]=N ,[t4]=N ,[t5]=N ,[t6]=N ,[t7]=N')
	sys.exit('[HX_AUTO_TEST]System initial Fail!')

# TODO: User definition, test items
t1 = sys.argv[1]
t2 = sys.argv[2]
t3 = sys.argv[3]
t4 = sys.argv[4]
if t4 == 'y':
	t4_times = sys.argv[9]
t5 = sys.argv[5]
if t5 == 'y':
	t5_times = sys.argv[10]
t6 = sys.argv[6]
if t6 == 'y':
	t6_times = sys.argv[11]
t7 = sys.argv[7]
if t7 == 'y':
	t7_times = sys.argv[12]
filename = sys.argv[8]

# TODO: read project file


# ============= function 1 test =============
if t1 == 'y':
	t1_ret = check_input_register()
	if t1_ret == True:
		print('[HX_AUTO_TEST]Check Input Register Test Pass!')
	else:
		print_status()
		sys.exit('[HX_AUTO_TEST]Check Input Register Test Fail!')

# ============= function 2 test =============
if t2 == 'y':
	# v1/v2 is for common v1/v2 driver
	debug_node_test_node_def(driver_ver)
	t2_ret = debug_node_test()
	if t2_ret == True:
		print('[HX_AUTO_TEST]Debug file node Test Pass!')
	else:
		print_status()
		sys.exit('[HX_AUTO_TEST]Debug file node Test Fail!')

# ============= function 3 test =============
if t3 == 'y':
	# v1/v2 is for common v1/v2 driver
	raw_out_sel_test_node_def(driver_ver)
	t3_ret = raw_out_sel_test()
	if t3_ret == True:
		print('[HX_AUTO_TEST]Raw data out Test Pass!')
	else:
		print_status()
		sys.exit('[HX_AUTO_TEST]Raw data out Test Fail!')

# ============= function 4 test =============
if t4 == 'y':
	t4_ret = inspection_test(t4_times)
	if t4_ret == True:
		print('[HX_AUTO_TEST]Inspection Test Pass!')
	else:
		print_status()
		sys.exit('[HX_AUTO_TEST]Inspection Test Fail!')

# ============= function 5 test =============
if t5 == 'y':
	t5_ret = fw_upgrade_test(t5_times)
	if t5_ret == True:
		print('[HX_AUTO_TEST]FW upgrade Test Pass!')
	else:
		print_status()
		sys.exit('[HX_AUTO_TEST]FW upgrade Test Fail!')

# ============= function 6 test =============
if t6 == 'y':
	t6_ret = suspend_resume_test(t6_times)
	if t6_ret == True:
		print('[HX_AUTO_TEST]Suspend Resume Test Pass!')
	else:
		print_status()
		sys.exit('[HX_AUTO_TEST]Suspend Resume Test Fail!')

# ============= function 7 test =============
if t7 == 'y':
	t7_ret = reboot_test(t7_times)
	if t7_ret == True:
		print('[HX_AUTO_TEST]Reboot Test Pass!')
	else:
		print_status()
		sys.exit('[HX_AUTO_TEST]Reboot Test Fail!')

print_status()


