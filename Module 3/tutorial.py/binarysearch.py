#User function template for Python

class Solution:	
    def binarysearch(self, arr, n, k):
        left= 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1

        return -1



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends