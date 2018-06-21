#include "graph.hpp"

graph::graph()
{
	std::cout<<"Initializing a new graph. \n";
	adj.clear();
	std::cin>>V;
	std::cin>>E;	
	for(int i=0; i<E;i++)
	{
		int v, w;
		std::cin>>v;
		std::cin>>w;
		addEdge(v, w);
	}
	std::cout<<"Graph initialized. \n";
}

int graph::V()
{
	return V;
}

int graph::E()
{
	return E;
}

void graph::addEdge(int v, int w)
{
	adj[v].push_back(w);
}

std::vector<int> graph::adj(int v)
{
	return adj[v];
}