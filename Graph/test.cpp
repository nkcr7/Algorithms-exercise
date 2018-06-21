#include "graph.hpp"
#include <iostream>

int main()
{
	graph = graph();
	for(int i=0;i<graph.V();i++)
	{
		std::cout<<"Vertex: "<<i<<"\n";
		std::cout<<"Connected edges: \n";
		for(int j=0; j<graph.adj[i].size();j++)
		{
			std::cout<<graph.adj[i][j]<<" ";
		}
		std::cout<<"\n\n";
	}
	return 0;
}