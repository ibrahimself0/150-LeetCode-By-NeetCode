import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        # import java.util.PriorityQueue;
        #
        # class KthLargest {
        #     private PriorityQueue<Integer> minHeap;
        #     private int k;
        #
        #     public KthLargest(int k, int[] nums) {
        #         this.k = k;
        #         this.minHeap = new PriorityQueue<>();
        #         for (int num : nums) {
        #             this.minHeap.offer(num);
        #         }
        #         while (this.minHeap.size() > k) {
        #             this.minHeap.poll();
        #         }
        #     }
        #
        #     public int add(int val) {
        #         this.minHeap.offer(val);
        #         if (this.minHeap.size() > this.k) {
        #             this.minHeap.poll();
        #         }
        #         return this.minHeap.peek();
        #     }
        # }
