const graph = {
  A: ["B"],
  B: ["A"],
  // A: ["B", "D"],
  // B: ["A", "C", "E"],
  // C: ["B"],
  // D: ["A", "E"],
  // E: ["B", "D", "F"],
  // F: ["E"],
};
let start = "A";

function dfs(graph, start) {
  let stack = [];
  let visited = new Set();
  stack.push(start);
  let result = [];
  while (stack.length > 0) {
    let node = stack.pop();
    if (!visited.has(node)) {
      visited.add(node);
      result.push(node);
      for (let i of graph[node]) {
        stack.push(i);
      }
    }
  }
  return result;
}

console.log(dfs(graph, start));
