import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { ListGroup, ListGroupItem, Spinner } from 'reactstrap'
import styles from '../styles/AnimeList.module.scss'
import { DownloadModal } from './DownloadAnimeModal'
import { SearchBar } from './SearchBar'
// import { VariableSizeGrid as Grid } from 'react-window'
// import { GridList, GridListTile, GridListTileBar } from '@material-ui/core'

export interface IAnime {
	id: any
	title: string
	episode_count: number
	anime_url: string
	count: number
}
const animeList: IAnime[] = []

export const AnimeList: React.FC = () => {
	const [list, setList]: [IAnime[], (list: IAnime[]) => void] =
		useState(animeList)
	const [flitredList, setFiltredList]: [IAnime[], (list: IAnime[]) => void] =
		useState(animeList)
	const [modal, setModal] = useState<boolean[]>([])
	const handleModal = (index: number): void => {
		setModal(prevState => {
			prevState[index] = !modal[index]
			return [...prevState]
		})
	}

	const handleSearch = (event: any): void => {
		let value = event.target.value
		let result = []
		result = list.filter((data: IAnime) => {
			const title = data.title.toLowerCase()
			return title.search(value) != -1
		})
		setFiltredList(result)
	}
	const mapList = flitredList.map((anime, index) => {
		return (
			<ListGroupItem
				tag="button"
				onClick={() => {
					handleModal(index)
				}}
			>
				{modal[index] && (
					<DownloadModal
						anime={anime}
						modal={modal[index]}
						toggle={handleModal}
						index={index}
					/>
				)}

				{anime.title}
			</ListGroupItem>
		)
	})

	useEffect(() => {
		axios
			.get<IAnime[]>('/api/animes/')
			.then(res => {
				setList(res.data)
				setFiltredList(res.data)
				setModal(() => {
					return Array(res.data.length).fill(false)
				})
			})
			.catch(err => console.error(err))
	}, [])

	let isLoaded

	if (list.length) {
		isLoaded = (
			// <GridList cols={3}>
			// 	{list.map((item, index) => (
			// 		<GridListTile key={item.id}>
			// 			<GridListTileBar title={item.title}></GridListTileBar>
			// 		</GridListTile>
			// 	))}
			// </GridList>
			<div style={{ flex: 1 }}>
				<SearchBar onChange={(e: any) => handleSearch(e)} />
				<ListGroup className={styles.list} key="id">
					{mapList}
				</ListGroup>
			</div>
		)
	} else {
		isLoaded = (
			<Spinner
				children=""
				style={{ margin: '30vh auto', width: '3rem', height: '3rem' }}
				color="primary"
			/>
		)
	}

	return <div className={styles.container}>{isLoaded}</div>
}
