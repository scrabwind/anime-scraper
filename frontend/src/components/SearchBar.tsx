import { fade, InputBase, makeStyles } from '@material-ui/core'
import { Search } from '@material-ui/icons'

const useStyles = makeStyles(theme => ({
	inputRoot: {
		color: 'inherit',
	},
	inputInput: {
		padding: theme.spacing(1, 1, 1, 0),
		// vertical padding + font size from searchIcon
		paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
		transition: theme.transitions.create('width'),
		width: '100%',
		[theme.breakpoints.up('md')]: {
			width: '20ch',
		},
	},
	search: {
		display: 'flex',
		position: 'relative',
		borderRadius: theme.shape.borderRadius,
		backgroundColor: fade(theme.palette.common.black, 0.15),
		'&:hover': {
			backgroundColor: fade(theme.palette.common.black, 0.25),
		},
		marginLeft: '67%',
		// justifyContent: 'flex-end',
		// width: '90%',
		// [theme.breakpoints.up('sm')]: {
		// 	marginLeft: theme.spacing(3),
		// 	width: 'auto',
		// },
	},
	searchIcon: {
		padding: theme.spacing(0, 2),
		height: '100%',
		position: 'absolute',
		pointerEvents: 'none',
		display: 'flex',
		alignItems: 'center',
		justifyContent: 'center',
	},
}))
interface Props {
	onChange: (e: object) => void
}
export const SearchBar = (props: Props) => {
	const classes = useStyles()
	return (
		<div className={classes.search}>
			<div className={classes.searchIcon}>
				<Search />
			</div>
			<InputBase
				placeholder="Search…"
				classes={{
					root: classes.inputRoot,
					input: classes.inputInput,
				}}
				inputProps={{ 'aria-label': 'search' }}
				onChange={props.onChange}
			/>
		</div>
	)
}
