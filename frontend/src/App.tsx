import React from 'react'
import logo from './logo.svg'
import { Route, Switch } from 'react-router-dom'

import { AnimeList } from './components/AnimeList'
import { Navigation } from './components/Navigation'
import { DownloadedAnimeList } from './components/DownloadedAnimeList'
const App: React.FC = () => {
	return (
		<div className="container-fluid">
			<div className="row">
				<main className="main-content col-lg-12 col-md-12 col-sm-12 p-0">
					<Navigation />
					<div className="main-content-container container-fluid px-4">
						<Route path="/list" component={AnimeList} />
						<Route path="/downloaded" component={DownloadedAnimeList} />
					</div>
				</main>
			</div>
		</div>
	)
}

export default App
