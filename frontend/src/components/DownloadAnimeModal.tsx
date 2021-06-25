import React, { useState } from 'react'
import {
	Button,
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

interface Values {
	toggle: boolean
}

interface Props {
	anime: IAnime
	modal: boolean
	index: number
	toggle: (index: number) => void
}
export const DownloadModal: React.FC<Props> = props => {
	const { anime, modal, toggle, index } = props
	// const [modal, setModal] = useState(false)
	// const toggle = () => setModal(!modal)
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
				// toggle={() => {
				// 	toggle(index)
				// }}
				>
					Download Anime
				</ModalHeader>
				<ModalBody>
					<Formik
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
								<label>Title: {anime.title}</label>
								<label>
									{'Download whole series: '}
									<Field type="checkbox" name="toggle" />
								</label>
							</Form>
						)}
					</Formik>
				</ModalBody>
				<ModalFooter>
					<Button
						color="primary"
						onClick={() => {
							toggle(index)
						}}
					>
						Click
					</Button>
				</ModalFooter>
			</Modal>
		</div>
	)
}
