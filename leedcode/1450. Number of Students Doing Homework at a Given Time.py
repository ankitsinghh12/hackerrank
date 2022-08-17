# https://donic0211.medium.com/leetocode-1450-number-of-students-doing-homework-at-a-given-time-cc5f67d731c2

class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        ans=0
        m=zip(startTime, endTime)
        for s, e in m:
            if s<=queryTime<=e:
                ans+=1
        return ans