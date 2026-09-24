class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] copyArray = new int[nums.length * 2]; 
        int[] finalArray = new int [nums.length + copyArray.length];

        for (int i = 0; i < copyArray.length; i++)
        {
            if (i < nums.length)
            {
                copyArray[i] = nums[i];
            }
            else {
                copyArray[i] = nums[i - nums.length];
            }

        }

        return copyArray; 
    }
}
