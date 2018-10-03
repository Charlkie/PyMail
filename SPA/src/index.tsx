import ApolloClient from "apollo-boost";
import * as React from 'react';
import { ApolloProvider } from "react-apollo"
import * as ReactDOM from 'react-dom';
import Home from './App';

const client = new ApolloClient({
  uri: "http://127.0.0.1:5000/graphql"
});

const App = () => (
	<ApolloProvider client={client}>
		<Home />
	</ApolloProvider>
)

ReactDOM.render(<App />,document.getElementById('root') as HTMLElement);
