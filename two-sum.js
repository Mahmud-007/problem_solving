// O(n^2)
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) {
        return [i, j];
      }
    }
  }
  return [];
};

// O(n logn)
const twosumTwoPointers = function (nums, target) {
  let temp = nums.map((num, i) => [num, i]);
  temp.sort((a, b) => {
    return a[0] - b[0];
  });
  let left = 0;
  let right = nums.length - 1;
  while (left < right) {
    let sum = temp[left][0] + temp[right][0];
    console.log({ sum, target });
    if (sum == target) {
      return [temp[left][1], temp[right][1]];
    } else if (sum > target) {
      right--;
    } else {
      left++;
    }
  }
  return [];
};

// O(n)
let twosumHashmap = function (nums, target) {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
    let remain = target - nums[i];
    let mapRemain = map.get(remain);
    console.log({ remain, mapRemain });
    if (map.has(remain)) {
      return [i, mapRemain];
    }
    map.set(nums[i], i);
  }
  return [];
};
let nums = [3,3], target = 6

console.log(twosumHashmap(nums, target));
