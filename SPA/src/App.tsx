import gql from "graphql-tag"
import * as React from 'react';
import { Query } from "react-apollo"

class Home extends React.Component {
  public render() {
	return (
		<div>
			<h1>Let's load some messages</h1>
			<Messages />
		</div>
	);
  }
}

const Messages = () => (
	<Query
		query={
			gql`
				{
					messages {
						id,
						name
					}
				}
			`
		}
	>
		{({ loading, error, data }) => {
			if (loading) { return <p>Loading...</p> }
			if (error) { return <p>Error :(</p> }

			return data.messages.map( ( {id, name}: {id: any, name: any} ) => (
				<div key={id}>
					<p>{name}</p>
				</div>
			))
		}}
	</Query>
)

export default Home;
