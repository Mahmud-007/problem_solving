const graph = {
  A: ["B", "D"],
  B: ["A", "C", "E"],
  C: ["B"],
  D: ["A", "E"],
  E: ["B", "D", "F"],
  F: ["E"],
};
let start = "A";

function bfs(graph, start) {
  let q = [];
  let visited = new Set();
  q.push(start);
  let result = [];
  while (q.length > 0) {
    let node = q.shift();
    if (!visited.has(node)) {
      visited.add(node);
      result.push(node);
      for (let i of graph[node]) {
        q.push(i);
      }
    }
  }
  return result;
}
console.log(bfs(graph, start));
