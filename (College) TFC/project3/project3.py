tapeInput = ''
tapeNumberA = []
tapeNumberB = []
tapeResult = []
headInput = 1
headA = 1
headB = 1
headResult = 1
headOperator = 1

def initTapes():
	global tapeNumberA
	global tapeNumberB
	global tapeResult

	for i in range(100):
		tapeNumberA.append(' ')
		tapeNumberB.append(' ')
		tapeResult.append(' ')

def q4():
	#print('q4')

	return True
#carry 1#
def q3():
	#print('q3')

	global tapeResult
	global tapeNumberA
	global tapeNumberB
	global headA
	global headB
	global headResult

	if(tapeNumberA[headA] == ' ' and tapeNumberB[headB] == ' '):
		tapeResult[headResult] = '1'
		return q4()
	if(tapeNumberA[headA] == '1' and tapeNumberB[headB] == '1'):
		tapeResult[headResult] = '1'
		headA -= 1
		headB -= 1
		headResult -= 1
		return q3()
	if(tapeNumberA[headA] == '0'):
		tapeNumberA[headA] = '1'
	elif(tapeNumberB[headB] == '0'):
		tapeNumberB[headB] = '1'
	return q2()


#sum#
def q2():
	#print('q2')

	global tapeResult
	global tapeNumberA
	global tapeNumberB
	global headA
	global headB
	global headResult

	if(tapeNumberA[headA] == ' ' and tapeNumberB[headB] == ' '):
		return q4()
	if(tapeNumberA[headA] == '1' and tapeNumberB[headB] == '1'):
		tapeResult[headResult] = '0'
		headA -= 1
		headB -= 1
		headResult -= 1
		return q3()
	if(tapeNumberA[headA] == '1' and tapeNumberB[headB] == '0'):
		tapeResult[headResult] = '1'
	if(tapeNumberA[headA] == '0' and tapeNumberB[headB] == '1'):
		tapeResult[headResult] = '1'
	if(tapeNumberA[headA] == '0' and tapeNumberB[headB] == '0'):
		tapeResult[headResult] = '0'
	headA -= 1
	headB -= 1
	headResult -= 1
	return q2()

#writing tape of second number#
def q1():
	#print('q1')
	global tapeInput
	global tapeNumberA
	global tapeNumberB
	global headA
	global headB
	global headInput
	global headResult

	if(tapeInput[headInput] == ' '):
		headA -= 1
		headB -= 1
		headResult -= 1
		return q2()
	elif(tapeInput[headInput] == '0'):
		tapeNumberB[headB] = '0'
	elif(tapeInput[headInput] == '1'):
		tapeNumberB[headB] = '1'
	else:
		return False
	headInput += 1
	headB += 1
	headResult += 1
	return q1()


#writing tape of first number#
def q0():
	#print('q0')
	global tapeInput
	global tapeNumberA
	global tapeNumberB
	global headA
	global headB
	global headInput

	##print(tapeInput[headInput])
	if(tapeInput[headInput] == '+'):
		headInput += 1
		return q1()
	elif(tapeInput[headInput] == '0'):
		tapeNumberA[headA] = '0'
	elif(tapeInput[headInput] == '1'):
		tapeNumberA[headA] = '1'
	else:
		return False
	headInput += 1
	headA += 1
	return q0()

initTapes()

tapeInput = input()
print(tapeInput)
tapeInput = ' ' + tapeInput + ' '
##print(tapeInput)
if(q0()):
	out = str(tapeResult)
	out = out.replace(' ', '')
	out = out.replace(',', '')
	out = out.replace('\'', '')
	out = out.replace('[', '')
	out = out.replace(']', '')
	tapeInput = tapeInput.replace(' ', '')
	print(tapeInput+'='+out+' ACEITA')
else:
	tapeInput = tapeInput.replace(' ', '')
	print(tapeInput+' REJEITA')
