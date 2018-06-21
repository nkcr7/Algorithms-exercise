#ifndef GRAPH_H
#define GRAPH_H

#include <iostream>
#include <vector>

class graph
{
private:
	int V; // 顶点数
	int E; // 边数
	std::vector<std::vector<int> > adj; // 邻接表
public:
	void graph();
	int V();
	int E();
	void addEdge(int v, int w);
	std::vector<int> adj(int v);
}




#endif

