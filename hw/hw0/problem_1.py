# 2/1/21, HW0

def main():
  #*******************************************************************************
  # 1A)
  # write a recursive function which returns the nth Fibonacci number
  # Ex.
  # (0) => 1
  # (1) => 1
  # (2) => 2
  # (3) => 3
  # (4) => 5
  # (5) => 8
  # (6) => 13
  # (7) => 21
  # f(n) => f(n - 1) + f(n - 2)
  # TIME COMPLEXITY:  O(2^N)     N = input number
  # SPACE COMPLEXITY: O(N)       N = Maximum depth of recursion tree (call stack)

  def nth_fibonacci(n):

    # error handling, if n < 0, exit
    if n < 0:
      return -1

    # base case if n is 0 or 1
    if n == 0 or n == 1:
      return 1
    
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

  # print(nth_fibonacci(-1))  #=> -1
  # print(nth_fibonacci(0))   #=> 1
  # print(nth_fibonacci(1))   #=> 1
  # print(nth_fibonacci(2))   #=> 2
  # print(nth_fibonacci(3))   #=> 3
  # print(nth_fibonacci(4))   #=> 5
  # print(nth_fibonacci(5))   #=> 8


  #*******************************************************************************
  # 1B)
  # Write a redumentary test to ensure the fibnoacci function behaves as expected
  # return None
  first_fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34]

  def test_fibs(first_fibs, nth_fibonacci):

    for index, num in enumerate(first_fibs):
      assert(first_fibs[index] == nth_fibonacci(index))

    print("All tests passed with no errors")

  test_fibs(first_fibs, nth_fibonacci)


  #*******************************************************************************
  # 1C)
  # Use Dynamic Programming to Cache/Memoize the values in the fib function
  import time

  class FibonacciMemo:

    def __init__(self):
      self.memo_dict = {0:1, 1:1}

    def fibonacci(self, n):
      if n in self.memo_dict:
        return self.memo_dict[n]

      self.memo_dict[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)

      return self.memo_dict[n]


  # initialize object
  fibonacci_memo = FibonacciMemo()

  # Timing the fib function
  first_run_start = time.time()
  fibonacci_memo.fibonacci(50)
  first_run_end = time.time()
  time_delta_1 = first_run_end - first_run_start

  # Second Run
  second_run_start = time.time()
  fibonacci_memo.fibonacci(50)
  second_run_end = time.time()
  time_delta_2 = second_run_end - second_run_start
  print(time_delta_1, time_delta_2)
  
  



if __name__ == '__main__':
  main()