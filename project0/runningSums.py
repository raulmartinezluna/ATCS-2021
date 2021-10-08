def runningSum(nums):
    runSum = 0
    completeSum = []
    for num in nums:
        runSum += num
        completeSum.append(runSum)
    return completeSum
