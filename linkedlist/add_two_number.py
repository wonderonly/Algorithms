#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse orde
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8

class ListNode(object):
  def __init__(self, val):
    self.val = val
    self.next = None

class Solution(object):
  def addTwoNumber(self, L1, L2):
    if L1 == None:
      return L2
    if L2 == None:
      return L1
    head = ListNode(0)
    carry = 0
    tail = head
    while L1 != None and L2 != None:
      tail.next = ListNode(0)
      tail = tail.next
      tail.val = L1.val + L2.val + carry
      carry = tail.val / 10
      tail.val = tail.val % 10
      L1 = L1.next
      L2 = L2.next
      
    while L1 != None:
      tail.next = L1
      tail = tail.next
      if carry != 0:
        tail.val = tail.val + carry
        carry = tail.val / 10
        tail.val = tail.val % 10
      else:
        break
      L1 = L1.next
 
    while L2 != None:
      tail.next = L2
      tail = tail.next
      if carry != 0:
        tail.val = tail.val + carry
        carry = tail.val / 10
        tail.val = tail.val % 10
      else:
        break
      L2 = L2.next
 
    if carry != 0: 
      tail.next = ListNode(0)
      tail.next.val = carry

    return head.next

  def addTwoNumber2(self, L1, L2):
    head = tail = ListNode(0)
    carry = 0
    while L1 or L2 or carry:
      val1 = val2 = 0
      if L1:
        val1 = L1.val
        L1 = L1.next
      if L2:
        val2 = L2.val
        L2 = L2.next
      sum = val1 + val2 + carry
      carry = sum / 10
      tail.next = ListNode(sum % 10)
      tail = tail.next
    return head.next

def test():
  head = ListNode(0)
  tail = head
  arr = [9, 8]
  for i in arr:
    tail.next = ListNode(i)
    tail = tail.next
  L1 = head.next

  arr = [1]
  tail = head
  for i in arr:
    tail.next = ListNode(i)
    tail = tail.next
  L2 = head.next

  sol = Solution()
 # ans1 = sol.addTwoNumber(L1, L2)
  ans1 = None
  ans2 = sol.addTwoNumber2(L1, L2)
  if ans1 is None:
    print 'ans1 is None'
  else:
    s1 = str(ans1.val)
    ans1 = ans1.next
    while ans1 != None:
      s1 = s1 + ' -> ' + str(ans1.val)
      ans1 = ans1.next
    print 's1 is: ' + s1
  if ans2 is None:
    print 'ans2 is None'
  else:
    s2 = str(ans2.val)
    ans2 = ans2.next
    while ans2 != None:
      s2 = s2 + ' -> ' + str(ans2.val)
      ans2 = ans2.next
    print 's2 is: ' + s2


if __name__ == "__main__":
  test()  
