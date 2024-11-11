class Solution:
  def maxArea(self, heights: List[int]) -> int:
      max_area = 0
      height_left = 0
      height_right = len(heights) - 1
      while height_left < height_right:
          area = min(heights[height_left], heights[height_right]) * (height_right - height_left)
          if area > max_area:
              max_area = area
          if heights[height_left] < heights[height_right]:
              height_left += 1
          else:
              height_right -= 1
      return max_area
