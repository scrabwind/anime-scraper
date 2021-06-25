import React, { useState } from 'react'
import { Link, NavLink as RRNavLink } from 'react-router-dom'
import {
	Collapse,
	Navbar,
	NavbarToggler,
	NavbarBrand,
	Nav,
	NavItem,
	NavLink,
	UncontrolledDropdown,
	DropdownToggle,
	DropdownMenu,
	DropdownItem,
	NavbarText,
} from 'reactstrap'

export const Navigation: React.FC = () => {
	const [isOpen, setIsOpen] = useState(false)

	const toggle = () => setIsOpen(!isOpen)

	return (
		<div>
			<Navbar color="light" light expand="md">
				<NavbarBrand href="/">dUwUloader</NavbarBrand>
				<NavbarToggler onClick={toggle} className="mr-2" />
				<Collapse isOpen={isOpen} navbar>
					<Nav className="ml-auto" navbar>
						<NavItem>
							<NavLink tag={RRNavLink} to="/list">
								Anime list
							</NavLink>
						</NavItem>
						<NavItem>
							<NavLink tag={RRNavLink} to="/downloaded">
								Downloaded anime
							</NavLink>
						</NavItem>
					</Nav>
				</Collapse>
			</Navbar>
		</div>
	)
}
