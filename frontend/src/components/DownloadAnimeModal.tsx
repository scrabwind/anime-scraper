import React, { useState, useEffect } from 'react'
import {
	Modal,
	ModalHeader,
	ModalBody,
	ModalFooter,
	Input,
	Label,
	Form,
	FormGroup,
} from 'reactstrap'
import { IAnime } from './AnimeList'
import styles from '../styles/DownloadModal.module.scss'
import { Field, Formik, FormikHelpers } from 'formik'
import {
	Grid,
	Typography,
	TextField,
	makeStyles,
	createStyles,
	Theme,
	Switch,
	FormControlLabel,
	Slider,
	Button,
} from '@material-ui/core'
import { GetApp } from '@material-ui/icons'
import axios from 'axios'
import Cookies from 'js-cookie'
import union from 'lodash.union'

interface Props {
	anime: IAnime
	modal: boolean
	index: number
	toggle: (index: number) => void
}

type Range = [number, number]

type Episodes = number[]
const sliderText = (value: number) => {
	return `${value} episode`
}
const getEpisodes = (range: Range): Episodes => {
	let episodes: Episodes = []
	for (let i = Math.min(...range); i < Math.max(...range) + 1; i++) {
		episodes.push(i)
	}
	return episodes
}
export const DownloadModal: React.FC<Props> = props => {
	const { anime, modal, toggle, index } = props
	const [checked, setChecked] = useState<boolean>(true)
	const [slider, setSlider] = useState<Range>([1, anime.episode_count])
	const handleChecked = (e: any) => {
		setChecked(!checked)
	}
	const handleSlider = (e: any, newValue: any) => {
		setSlider(newValue)
	}

	const downloadRequest = (slider: Range) => {
		const sliderEpisodes = getEpisodes(slider)
		try {
			axios.get(`/api/downloadedAnimes?anime=${anime.id}`).then(res => {
				const data = res.data[0]
				if (data) {
					let episodes: Episodes = union(data.episodes, sliderEpisodes)
					episodes = episodes.sort((a: number, b: number) => a - b)
					axios.patch(
						`/api/downloadedAnimes/${data.id}/`,
						{ episodes: episodes },
						{
							headers: {
								'X-CSRFToken': Cookies.get('csrftoken'),
							},
						}
					)
				} else {
					const payload = {
						anime: anime.id,
						episodes: sliderEpisodes,
					}
					axios.post('/api/downloadedAnimes/', payload, {
						headers: {
							'X-CSRFToken': Cookies.get('csrftoken'),
						},
					})
				}
			})
		} catch (err) {
			console.error(err)
		}
	}
	// const [modal, setModal] = useState(false)
	// const toggle = () => setModal(!modal)
	let isVisible
	// useEffect(() => {}, [modal])
	if (!checked) {
		isVisible = (
			<Slider
				value={slider}
				onChange={handleSlider}
				aria-labelledby="range-slider"
				getAriaValueText={sliderText}
				valueLabelDisplay="auto"
				min={1}
				max={anime.episode_count}
			/>
		)
	}
	return (
		<div>
			<Modal
				isOpen={modal}
				toggle={() => {
					toggle(index)
				}}
				backdrop={true}
				centered={true}
				contentClassName={styles.modal}
			>
				<ModalHeader
					className={styles.modalHeader}
					// toggle={() => {
					// 	toggle(index)
					// }}
				>
					Download Anime
				</ModalHeader>
				<ModalBody className={styles.modalBody}>
					{/* <Formik
						initialValues={{ toggle: true }}
						onSubmit={(values: Values, { setSubmitting }: FormikHelpers<Values>) => {
							setTimeout(() => {
								alert(JSON.stringify(values, null, 2))
								setSubmitting(false)
							}, 500)
						}}
					>
						{({ values }) => (
							<Form className={styles.form}>
								<label>
									{'Download whole series: '}
									<Field type="checkbox" name="toggle" />
								</label>
							</Form>
						)}
					</Formik> */}
					<div className={styles.title}>
						<Typography className={styles.titleLabel} variant={'body1'}>
							Title:
						</Typography>
						<Typography variant={'body1'}>{anime.title}</Typography>
					</div>
					<div className={styles.download}>
						<FormControlLabel
							control={
								<Switch checked={checked} onChange={handleChecked} color="primary" />
							}
							label="Download whole series"
						/>
						{isVisible}
					</div>
				</ModalBody>
				<ModalFooter>
					<Button
						color="primary"
						onClick={() => {
							toggle(index)
							downloadRequest(slider)
						}}
						variant="contained"
						startIcon={<GetApp />}
					>
						Download
					</Button>
				</ModalFooter>
			</Modal>
		</div>
	)
}
