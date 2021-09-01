module Metropolis_for_2D_Ising

contains

	subroutine Metropolis(J, H, k_B, T, L, t_END, Energy, Magnetization)

		real (kind = 8), intent(in) :: J, H, k_B, T
		integer, intent(in) :: L, t_END
		
		real (kind = 8) :: Delta_H
		integer :: AllocateStatus, i
		
		integer, dimension(2) :: candidate
		integer, dimension(4) :: neighbors
		
		integer, dimension(:,:), allocatable :: spins
		
		real (kind = 8), dimension(t_END+1), intent(out) :: Energy, Magnetization
		
		! Definindo estado inicial
		allocate(spins(L,L), stat = AllocateStatus)
		if (AllocateStatus /= 0) stop '*** Not enough memory ***'
		spins = 1
		
		! Iniciando vetores de energia e magnetização
		Energy(1) = 0
		Magnetization(1) = sum(spins)
		
		do i=1, t_END
		
			candidate = (/ Random_Integer(1,L), Random_Integer(1,L) /)
			neighbors = (/ spins(L*(1-merge(0,1,(candidate(1)-1)==0))+(candidate(1)-1),candidate(2)),&
					&spins(mod(candidate(1),L)+1,candidate(2)),&
					&spins(candidate(1),L*(1-merge(0,1,(candidate(2)-1)==0))+(candidate(2)-1)), &
					&spins(candidate(1),mod(candidate(2),L)+1) /)
					
			Energy(i+1) = Energy(i)
			Magnetization(i+1) = Magnetization(i)
			Delta_H = 2 * spins(candidate(1),candidate(2)) * (J*sum(neighbors) + H)
			
			if ( (Delta_H < 0) .or. (rand() <= exp(-Delta_H/(k_B*T))) ) then
				!print *,Delta_H
				!print *,'Transicionou'
				spins(candidate(1),candidate(2)) = -1*spins(candidate(1),candidate(2))
				
				Energy(i+1) = Energy(i) + Delta_H
				Magnetization(i+1) = Magnetization(i) + 2*spins(candidate(1),candidate(2))
				   
			end if
			
		end do
		
	end subroutine Metropolis
	
	function Random_Integer(n,m)
		!integer :: n, m
		real (kind = 8) :: u
		
		call random_number(u)
		Random_Integer = n + FLOOR((m+1-n)*u)

	end function Random_Integer

end module Metropolis_for_2D_Ising
